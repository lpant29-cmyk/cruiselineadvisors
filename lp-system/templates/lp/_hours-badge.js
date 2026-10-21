/* "Advisors answering now" must be true at the moment it says it.

   Coverage is 8am-11pm ET every day (Hard Rule 6: never claim 24/7). The badge
   was static markup, so at 3am it still told visitors someone was answering,
   and the green live-dot said the same thing in colour.

   The hour is read in America/New_York, not on the visitor's clock: a visitor
   in London at 1pm is looking at an 8am ET office, and our own clock is what
   decides whether anyone is there. Intl handles the DST switch by itself, so
   there is no offset to maintain twice a year.

   Fails open-safe: if Intl is unavailable the markup is left exactly as shipped
   rather than guessed at, and the whole thing is wrapped so a throw here can
   never take down the scripts after it. */
(function () {
  var OPEN_HOUR = 8, CLOSE_HOUR = 23;   // 8am to 11pm, inclusive of 10:59pm
  var hour;
  try {
    hour = +new Intl.DateTimeFormat("en-US", {
      timeZone: "America/New_York", hour: "numeric", hour12: false,
    }).format(new Date());
  } catch (e) {
    return;
  }
  if (!isFinite(hour) || (hour >= OPEN_HOUR && hour < CLOSE_HOUR)) return;

  var CLOSED = "Call now. Advisors back at 8am ET";
  var now = document.querySelector(".topbar .now");
  if (now) now.textContent = CLOSED + " · ";

  var metas = document.querySelectorAll(".callmeta span, .hours");
  for (var i = 0; i < metas.length; i++) {
    var el = metas[i];
    if (!/advisors answering now/i.test(el.textContent)) continue;
    // keep whatever structure the element already has, swap only the claim
    el.innerHTML = el.innerHTML.replace(/Advisors answering now/i, CLOSED);
  }

  // The green dot reads as "live" on its own, so it goes quiet too.
  var dots = document.querySelectorAll(".dot, .callmeta b");
  for (var j = 0; j < dots.length; j++) dots[j].style.background = "transparent";
  for (var k = 0; k < dots.length; k++) {
    if (dots[k].tagName === "B") dots[k].style.color = "#8aa0ab";
  }
})();
