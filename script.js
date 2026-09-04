/* Mobile nav ------------------------------------------------ */
const menuButton = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (menuButton && navLinks) {
  menuButton.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(open));
  });
  // close the menu after jumping to a section
  navLinks.addEventListener('click', (e) => {
    if (e.target.tagName === 'A' && navLinks.classList.contains('open')) {
      navLinks.classList.remove('open');
      menuButton.setAttribute('aria-expanded', 'false');
    }
  });
}

/* Current year in the footer -------------------------------- */
document.querySelectorAll('#year, .year').forEach((el) => {
  el.textContent = new Date().getFullYear();
});

/* Skill filter ---------------------------------------------- */
/* Select any number of skills; the timeline keeps every project
   that uses at least one of them. No selection means show all.  */
(() => {
  const filter = document.querySelector('[data-filter]');
  const track = document.querySelector('[data-track]');
  if (!filter || !track) return;

  const chips = [...filter.querySelectorAll('.chip')];
  const entries = [...track.querySelectorAll('.entry')];
  const status = filter.querySelector('[data-status]');
  const clearBtn = filter.querySelector('[data-clear]');
  const emptyMsg = track.querySelector('[data-empty-msg]');
  const total = entries.length;

  const skillsOf = (el) => (el.dataset.skills || '').split(' ').filter(Boolean);
  const selected = new Set();

  function apply() {
    let shown = 0;

    entries.forEach((entry) => {
      const skills = skillsOf(entry);
      const match = selected.size === 0 || skills.some((s) => selected.has(s));
      entry.hidden = !match;
      if (match) shown += 1;

      // highlight the tags inside a card that caused the match
      entry.querySelectorAll('.tag').forEach((tag) => {
        tag.dataset.on = selected.has(tag.dataset.skill) ? 'true' : 'false';
      });
    });

    // dim any skill that would return nothing on top of the current selection
    chips.forEach((chip) => {
      const skill = chip.dataset.skill;
      if (chip.dataset.goto) { chip.dataset.empty = 'false'; return; }
      if (selected.has(skill)) { chip.dataset.empty = 'false'; return; }
      const anywhere = entries.some((e) => skillsOf(e).includes(skill));
      chip.dataset.empty = anywhere ? 'false' : 'true';
    });

    if (status) {
      status.innerHTML = selected.size === 0
        ? `Showing all <strong>${total}</strong> projects`
        : `Showing <strong>${shown}</strong> of ${total} projects`;
    }
    if (clearBtn) clearBtn.hidden = selected.size === 0;
    if (emptyMsg) emptyMsg.hidden = shown !== 0;
  }

  chips.forEach((chip) => {
    chip.addEventListener('click', () => {
      if (chip.dataset.goto) { window.location.href = chip.dataset.goto; return; }
      const skill = chip.dataset.skill;
      const on = !(chip.getAttribute('aria-pressed') === 'true');
      chip.setAttribute('aria-pressed', String(on));
      on ? selected.add(skill) : selected.delete(skill);
      apply();
    });
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', (ev) => {
      ev.preventDefault();   // the button sits inside <summary>
      ev.stopPropagation();  // so don't let the click collapse the panel
      selected.clear();
      chips.forEach((c) => c.setAttribute('aria-pressed', 'false'));
      apply();
      if (chips[0]) chips[0].focus();
    });
  }

  // the chip list is tall on a phone, so start it collapsed there
  if (filter.tagName === 'DETAILS' && window.matchMedia('(max-width: 760px)').matches) {
    filter.open = false;
  }

  apply();
})();
