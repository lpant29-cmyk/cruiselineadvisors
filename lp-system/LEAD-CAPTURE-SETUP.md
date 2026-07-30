# Callback form -> Google Sheet (cruise leads tab)

Goal: the "Prefer we call you?" form on every /go/ page drops its lead into
a **new tab on the existing sheet** that already receives flight-booking
requests from the other site. No server, no new service, ~10 minutes.

The pages already collect name, phone and best-time-to-call, and already
fire a `lead_submit` dataLayer event. They just have nowhere to post yet
(`action="#CALLBACK_ACTION"` is a placeholder that shows the thank-you but
transmits nothing). This wires the real endpoint.

---

## Step 1 — add the tab (you, in the sheet)

In the existing spreadsheet, add a tab named exactly **`cruise_leads`** with
this header row:

| timestamp | name | phone | best_time | page_id | page_url | lp_variant | lp_when | source |
|---|---|---|---|---|---|---|---|---|

Keeping cruise leads on the same spreadsheet as the flight leads means one
place to watch; the `source` column keeps them separable.

## Step 2 — add the script (you, 2 minutes)

In that spreadsheet: **Extensions > Apps Script**, delete whatever is there,
paste this, and save.

```javascript
// Cruise LP callback form -> cruise_leads tab.
// Deployed as a web app; the /go/ pages POST to its URL.
const TAB = 'cruise_leads';

function doPost(e) {
  try {
    const p = (e && e.parameter) || {};
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(TAB);
    if (!sheet) throw new Error('Tab ' + TAB + ' not found');
    sheet.appendRow([
      new Date(),
      p.name || '',
      p.phone || '',
      p.calltime || '',
      p.page_id || '',
      p.page_url || '',
      p.lp_variant || '',
      p.lp_when || '',
      'cruise-lp'
    ]);
    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

Optional but recommended, so a lead reaches you even if nobody is watching
the sheet. Add inside `doPost`, just before the `return`:

```javascript
    MailApp.sendEmail({
      to: 'YOUR@EMAIL.COM',
      subject: 'Cruise callback request: ' + (p.name || 'no name'),
      body: [p.name, p.phone, p.calltime, p.page_url].join('\n')
    });
```

## Step 3 — deploy it (you)

**Deploy > New deployment > type: Web app.**
- Description: `cruise LP callback`
- Execute as: **Me**
- Who has access: **Anyone**   <- required, the visitor is not signed in

Authorize when prompted (it will warn that the script is unverified; it is
your own script). Copy the **Web app URL** — it looks like
`https://script.google.com/macros/s/AKfy..../exec`.

## Step 4 — give me the URL

Send it and I will set it as the form action, rebake and re-verify. After
that a real submission writes a row and `lead_submit` fires with
`form_mode:'live'` instead of `'placeholder'`, so real leads are
distinguishable from test traffic in GTM.

---

## Until the URL exists

The form must not silently discard leads on a live page. Two options:

- **(a) Launch call-only** — the callback form is replaced by a "Call us"
  block until the endpoint is ready. Nothing is lost; the phone is the
  primary conversion anyway.
- **(b) Hold the launch** until step 4 is done (about ten minutes of work).

Default if nothing is decided: **(a)**, because a form that eats leads is
worse than no form.

## Notes

- No API key or secret sits in the page; the Apps Script URL is the whole
  credential, and it can only append rows to that one tab.
- TCPA consent line and the link to the consent page are already on the
  form, and the consent text is stored with nothing extra needed.
- If the sheet ever moves, only the Apps Script binding changes; the page
  keeps posting to the same URL.
