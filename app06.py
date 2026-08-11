<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>Discipline Hub | Student Productivity Mobile App</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Stylesheet -->
  <link rel="stylesheet" href="./src/style.css" />

  <!-- Mobile & PWA meta -->
  <meta name="theme-color" content="#090d16" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="description" content="Ultimate self-discipline, focus study timer, habit tracker, and timetable app for students." />

  <!-- CDN Dependencies for direct browser execution without build step -->
  <script src="https://cdn.jsdelivr.net/npm/lucide@latest/dist/umd/lucide.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
</head>
<body class="bg-dark text-light font-sans antialiased mobile-frame-disabled">
  <div id="app-container" class="app-viewport">
    <!-- Simulated Phone Wrapper container (toggled via button) -->
    <div id="phone-shell" class="phone-shell">
      <div class="phone-camera-notch"></div>
      
      <!-- Android Status Bar -->
      <div class="android-status-bar">
        <span class="status-time" id="status-clock">09:41</span>
        <div class="status-icons">
          <i data-lucide="wifi" class="icon-sm"></i>
          <i data-lucide="signal" class="icon-sm"></i>
          <i data-lucide="battery-charging" class="icon-sm"></i>
        </div>
      </div>

      <!-- App Header -->
      <header class="app-header">
        <div class="header-left">
          <div class="user-avatar" id="btn-user-profile">
            <span id="user-initials">AS</span>
            <span class="online-indicator"></span>
          </div>
          <div class="user-meta">
            <h1 class="app-title">Discipline Hub</h1>
            <div class="level-badge">
              <span id="user-rank-title">Scholar LVL 1</span>
              <div class="xp-mini-bar"><div id="xp-bar-fill" style="width: 20%"></div></div>
            </div>
          </div>
        </div>
        <div class="header-right">
          <button id="toggle-device-frame" class="icon-btn" title="Toggle Mobile Shell Frame">
            <i data-lucide="smartphone"></i>
          </button>
          <button id="btn-notifications" class="icon-btn badge-dot" title="Daily Motivational Coach">
            <i data-lucide="sparkles"></i>
          </button>
        </div>
      </header>

      <!-- Main View Content Area -->
      <main id="main-content" class="main-content-scroll">
        <!-- Dynamic render target for active tab -->
      </main>

      <!-- Android Bottom Navigation Bar -->
      <nav class="bottom-nav">
        <button class="nav-item active" data-tab="dashboard">
          <i data-lucide="layout-dashboard"></i>
          <span>Hub</span>
        </button>
        <button class="nav-item" data-tab="timer">
          <i data-lucide="timer"></i>
          <span>Focus</span>
        </button>
        <button class="nav-item" data-tab="habits">
          <i data-lucide="check-circle-2"></i>
          <span>Habits</span>
        </button>
        <button class="nav-item" data-tab="tasks">
          <i data-lucide="list-todo"></i>
          <span>Tasks</span>
        </button>
        <button class="nav-item" data-tab="timetable">
          <i data-lucide="calendar"></i>
          <span>Schedule</span>
        </button>
        <button class="nav-item" data-tab="analytics">
          <i data-lucide="bar-chart-3"></i>
          <span>Stats</span>
        </button>
      </nav>
      
      <!-- Android Gesture Home Indicator Bar -->
      <div class="android-home-indicator"></div>
    </div>
  </div>

  <!-- Global Modal Container -->
  <div id="modal-overlay" class="modal-overlay hidden">
    <div class="modal-card" id="modal-box">
      <button class="modal-close" id="btn-close-modal">&times;</button>
      <div id="modal-content"></div>
    </div>
  </div>

  <!-- Strict Mode Lockdown Overlay -->
  <div id="strict-mode-overlay" class="strict-mode-overlay hidden">
    <div class="strict-shield-box">
      <div class="shield-icon pulse">
        <i data-lucide="shield-alert" class="icon-xl"></i>
      </div>
      <h2>STRICT DISCIPLINE MODE ACTIVE</h2>
      <p class="strict-warning">Digital Detox in progress. Phone distraction features disabled!</p>
      <div class="strict-timer-display" id="strict-countdown">25:00</div>
      <div class="strict-quote" id="strict-quote">"Discipline is choosing between what you want now and what you want most."</div>
      <button id="btn-emergency-unlock" class="btn btn-outline-danger btn-sm">Give Up (Lose 50 XP & Reset Streak)</button>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div id="toast-container" class="toast-container"></div>

  <script type="module" src="./src/main.js"></script>
</body>
</html>









     



























