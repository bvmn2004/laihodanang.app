/**
 * NHƯ Ý DRIVER - CORE JAVASCRIPT ES6+
 * Website: https://laihodanang.app
 * Hotline: 0985 666 044
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initDropdownMenu();
  initFaqAccordion();
  initFareCalculator();
  initHeaderScroll();
  initTracking();
});

/* ==========================================================================
   1. MOBILE MENU DRAWER
   ========================================================================== */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobileMenuToggle');
  const drawer = document.getElementById('mobileNavDrawer');
  const closeBtn = document.getElementById('mobileDrawerClose');

  if (!toggleBtn || !drawer) return;

  function openMenu() {
    drawer.classList.add('active');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    toggleBtn.setAttribute('aria-expanded', 'true');
    if (closeBtn) closeBtn.focus();
  }

  function closeMenu() {
    drawer.classList.remove('active');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    toggleBtn.setAttribute('aria-expanded', 'false');
    toggleBtn.focus();
  }

  toggleBtn.addEventListener('click', openMenu);
  if (closeBtn) closeBtn.addEventListener('click', closeMenu);

  // Close when clicking outside content
  drawer.addEventListener('click', (e) => {
    if (e.target === drawer) closeMenu();
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('active')) {
      closeMenu();
    }
  });
}

/* ==========================================================================
   2. DESKTOP & ACCESSIBLE DROPDOWN MENU
   ========================================================================== */
function initDropdownMenu() {
  const dropdownItems = document.querySelectorAll('.nav-item-dropdown');
  if (!dropdownItems.length) return;

  function closeAllDropdowns() {
    dropdownItems.forEach((item) => {
      item.classList.remove('is-open');
      const toggle = item.querySelector('.dropdown-toggle');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    });
  }

  dropdownItems.forEach((item) => {
    const toggle = item.querySelector('.dropdown-toggle');
    const menu = item.querySelector('.nav-dropdown-menu');
    if (!toggle || !menu) return;

    // Click toggle for mouse or touch
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const isOpen = item.classList.contains('is-open');
      closeAllDropdowns();
      if (!isOpen) {
        item.classList.add('is-open');
        toggle.setAttribute('aria-expanded', 'true');
      }
    });

    // Hover sync for ARIA
    item.addEventListener('mouseenter', () => {
      toggle.setAttribute('aria-expanded', 'true');
    });
    item.addEventListener('mouseleave', () => {
      if (!item.classList.contains('is-open')) {
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    // Keyboard navigation within dropdown
    item.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeAllDropdowns();
        toggle.focus();
      }
    });
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', (e) => {
    let insideDropdown = false;
    dropdownItems.forEach((item) => {
      if (item.contains(e.target)) {
        insideDropdown = true;
      }
    });
    if (!insideDropdown) {
      closeAllDropdowns();
    }
  });
}

/* ==========================================================================
   3. FAQ ACCORDION
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  if (!faqItems.length) return;

  faqItems.forEach((item) => {
    const questionBtn = item.querySelector('.faq-question-btn');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all other FAQs for clean single-view accordion
      faqItems.forEach((other) => {
        if (other !== item) {
          other.classList.remove('active');
          const btn = other.querySelector('.faq-question-btn');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        }
      });

      // Toggle current
      if (isActive) {
        item.classList.remove('active');
        questionBtn.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

/* ==========================================================================
   4. INTERACTIVE FARE CALCULATOR
   ========================================================================== */
function initFareCalculator() {
  const calcBox = document.getElementById('fareCalculator');
  if (!calcBox) return;

  const vehicleSelect = document.getElementById('calcVehicle');
  const distanceInput = document.getElementById('calcDistance');
  const nightToggle = document.getElementById('calcNightTime');
  const resultPrice = document.getElementById('calcResultPrice');
  const resultBreakdown = document.getElementById('calcResultBreakdown');
  const quickDistanceBtns = document.querySelectorAll('.calc-quick-km');

  function calculateFare() {
    const vehicle = vehicleSelect ? vehicleSelect.value : 'oto';
    const km = parseFloat(distanceInput ? distanceInput.value : 0) || 0;
    const isNight = nightToggle ? nightToggle.checked : false;

    let total = 0;
    let breakdown = '';
    const nightFee = isNight ? 50000 : 0;
    const nightText = isNight ? ' (+50.000đ phụ phí đêm sau 23h)' : '';

    if (vehicle === 'oto') {
      // Ô TÔ PRICING RULES:
      // 0 - 5 km: 150.000đ
      // 5 - 10 km: 200.000đ
      // 10 - 30 km: 200.000đ + (km - 10) * 15.000đ
      // > 30 km: Thỏa thuận
      if (km <= 0) {
        total = 150000 + nightFee;
        breakdown = `Khung 0 - 5 km cố định: 150.000đ${nightText}`;
      } else if (km <= 5) {
        total = 150000 + nightFee;
        breakdown = `Quãng đường ${km} km (Khung 0 - 5 km cố định): 150.000đ${nightText}`;
      } else if (km <= 10) {
        total = 200000 + nightFee;
        breakdown = `Quãng đường ${km} km (Khung 5 - 10 km cố định): 200.000đ${nightText}`;
      } else if (km <= 30) {
        const extraKm = km - 10;
        const extraCost = extraKm * 15000;
        total = 200000 + extraCost + nightFee;
        breakdown = `10 km đầu (200.000đ) + ${extraKm.toFixed(1)} km × 15.000đ/km (${formatVND(extraCost)})${nightText}`;
      } else {
        total = null;
        breakdown = `Quãng đường trên 30 km thuộc tuyến đường dài / đi tỉnh. Vui lòng liên hệ Hotline 0985 666 044 để nhận giá ưu đãi nhất!`;
      }
    } else {
      // XE MÁY PRICING RULES:
      // 0 - 5 km: 110.000đ
      // 5 - 7 km: 130.000đ
      // 7 - 10 km: 170.000đ
      // > 10 km: +10.000đ/km
      if (km <= 0 || km <= 5) {
        total = 110000 + nightFee;
        breakdown = `Quãng đường ${km || '<5'} km (Khung 0 - 5 km cố định): 110.000đ${nightText}`;
      } else if (km <= 7) {
        total = 130000 + nightFee;
        breakdown = `Quãng đường ${km} km (Khung 5 - 7 km): 130.000đ${nightText}`;
      } else if (km <= 10) {
        total = 170000 + nightFee;
        breakdown = `Quãng đường ${km} km (Khung 7 - 10 km): 170.000đ${nightText}`;
      } else {
        const extraKm = km - 10;
        const extraCost = extraKm * 10000;
        total = 170000 + extraCost + nightFee;
        breakdown = `10 km đầu (170.000đ) + ${extraKm.toFixed(1)} km × 10.000đ/km (${formatVND(extraCost)})${nightText}`;
      }
    }

    if (resultPrice) {
      if (total !== null) {
        resultPrice.textContent = formatVND(total);
      } else {
        resultPrice.textContent = 'Giá Thỏa Thuận';
      }
    }
    if (resultBreakdown) {
      resultBreakdown.textContent = breakdown;
    }
  }

  function formatVND(num) {
    return new Intl.NumberFormat('vi-VN').format(num) + 'đ';
  }

  if (vehicleSelect) vehicleSelect.addEventListener('change', calculateFare);
  if (distanceInput) distanceInput.addEventListener('input', calculateFare);
  if (nightToggle) nightToggle.addEventListener('change', calculateFare);

  quickDistanceBtns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const kmVal = btn.getAttribute('data-km');
      if (distanceInput && kmVal) {
        distanceInput.value = kmVal;
        calculateFare();
      }
    });
  });

  // Run on start
  calculateFare();
}

/* ==========================================================================
   5. HEADER SCROLL ELEVATION
   ========================================================================== */
function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* ==========================================================================
   6. CONVERSION TRACKING HELPER
   ========================================================================== */
function initTracking() {
  const callLinks = document.querySelectorAll('a[href^="tel:"]');
  const zaloLinks = document.querySelectorAll('a[href*="zalo.me"]');
  const fbLinks = document.querySelectorAll('a[href*="facebook.com"]');

  callLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'click_hotline_call', {
          event_category: 'Contact',
          event_label: '0985 666 044'
        });
      }
    });
  });

  zaloLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'click_zalo_booking', {
          event_category: 'Contact',
          event_label: 'Zalo 0985 666 044'
        });
      }
    });
  });

  fbLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'click_facebook_contact', {
          event_category: 'Contact',
          event_label: 'Facebook Như Ý Driver'
        });
      }
    });
  });
}
