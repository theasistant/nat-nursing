#!/usr/bin/env python3
"""Generate the complete NoT Nurse HTML file."""

import os

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return len(content)

# The CSS
CSS = open('/dev/stdin', 'r') if False else None  # placeholder

# Build CSS
css = """
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100;200;300;400;500;600;700;800;900&display=swap');
:root{--bg-primary:#0a0e27;--bg-secondary:#1a1a3e;--bg-card:rgba(26,26,62,0.6);--primary:#6c5ce7;--primary-light:#a29bfe;--accent:#00cec9;--success:#00b894;--warning:#fdcb6e;--danger:#e17055;--text:#e0e0e0;--text-secondary:#a0a0b8;--text-muted:#6c6c8a;--border:rgba(108,92,231,0.2);--sidebar-width:260px;--topbar-height:65px;--radius:16px;--radius-sm:10px;--transition:all 0.3s cubic-bezier(0.4,0,0.2,1)}
*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}body{font-family:'Vazirmatn',sans-serif;background:var(--bg-primary);color:var(--text);direction:rtl;min-height:100vh;overflow-x:hidden}
::-webkit-scrollbar{width:8px}::-webkit-scrollbar-track{background:var(--bg-primary)}::-webkit-scrollbar-thumb{background:var(--primary);border-radius:4px}::-webkit-scrollbar-thumb:hover{background:var(--primary-light)}
.bg-animated{position:fixed;top:0;left:0;width:100%;height:100%;background:linear-gradient(-45deg,#0a0e27,#1a1a3e,#16213e,#0f3460,#1a1a3e,#0a0e27);background-size:400% 400%;animation:gradientMove 20s ease infinite;z-index:-2}
@keyframes gradientMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.particles{position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;pointer-events:none;overflow:hidden}
.particle{position:absolute;border-radius:50%;background:var(--primary);opacity:0.15;animation:floatParticle linear infinite}
@keyframes floatParticle{0%{transform:translateY(100vh) rotate(0deg);opacity:0}10%{opacity:0.15}90%{opacity:0.15}100%{transform:translateY(-100px) rotate(720deg);opacity:0}}
#loading-screen{position:fixed;top:0;left:0;width:100%;height:100%;background:var(--bg-primary);z-index:10000;display:flex;align-items:center;justify-content:center;flex-direction:column;transition:opacity 0.5s,visibility 0.5s}
#loading-screen.hidden{opacity:0;visibility:hidden;pointer-events:none}
.loader-logo{font-size:48px;font-weight:900;color:var(--primary);margin-bottom:30px;animation:pulse 2s ease-in-out infinite}
.loader-logo span{color:var(--accent)}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
.loader-bar{width:200px;height:4px;background:rgba(108,92,231,0.2);border-radius:2px;overflow:hidden}
.loader-bar-inner{width:0;height:100%;background:linear-gradient(90deg,var(--primary),var(--accent));border-radius:2px;animation:loadBar 1.5s ease-out forwards}
@keyframes loadBar{to{width:100%}}
.loader-text{margin-top:15px;color:var(--text-secondary);font-size:14px}
.sidebar{position:fixed;top:0;right:0;width:var(--sidebar-width);height:100vh;background:rgba(10,14,39,0.95);backdrop-filter:blur(20px);border-left:1px solid var(--border);z-index:1000;display:flex;flex-direction:column;transition:transform 0.3s ease}
.sidebar-header{padding:20px;text-align:center;border-bottom:1px solid var(--border)}
.sidebar-logo{font-size:24px;font-weight:900}.sidebar-logo .logo-not{color:var(--primary)}.sidebar-logo .logo-nurse{color:var(--accent)}
.sidebar-nav{flex:1;overflow-y:auto;padding:10px}
.nav-item{display:flex;align-items:center;gap:12px;padding:12px 16px;border-radius:var(--radius-sm);cursor:pointer;transition:var(--transition);color:var(--text-secondary);margin-bottom:4px;position:relative}
.nav-item:hover{background:rgba(108,92,231,0.1);color:var(--text);transform:translateX(-4px)}
.nav-item.active{background:rgba(108,92,231,0.2);color:var(--primary-light);border:1px solid var(--border)}
.nav-item.active::before{content:'';position:absolute;right:0;top:50%;transform:translateY(-50%);width:3px;height:60%;background:var(--primary);border-radius:3px 0 0 3px}
.nav-icon{font-size:20px;width:28px;text-align:center}.nav-label{font-size:14px;font-weight:500}
.sidebar-footer{padding:15px 20px;border-top:1px solid var(--border);text-align:center}
.sidebar-footer .version{font-size:12px;color:var(--text-muted)}
.topbar{position:fixed;top:0;right:var(--sidebar-width);left:0;height:var(--topbar-height);background:rgba(10,14,39,0.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 24px;z-index:999;transition:right 0.3s ease}
.topbar-left{display:flex;align-items:center;gap:12px}.topbar-right{display:flex;align-items:center;gap:16px}
.hamburger{display:none;background:none;border:none;color:var(--text);font-size:24px;cursor:pointer}
.topbar-user{display:flex;align-items:center;gap:10px}
.user-avatar{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--accent));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px}
.user-name{font-weight:600;font-size:14px}
.topbar-btn{width:40px;height:40px;border-radius:12px;border:1px solid var(--border);background:rgba(108,92,231,0.1);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:var(--transition);position:relative}
.topbar-btn:hover{background:rgba(108,92,231,0.2);color:var(--text);transform:scale(1.05)}
.notif-badge{position:absolute;top:-4px;left:-4px;width:18px;height:18px;background:var(--danger);border-radius:50%;font-size:10px;display:flex;align-items:center;justify-content:center}
.main-content{margin-right:var(--sidebar-width);margin-top:var(--topbar-height);padding:24px;min-height:calc(100vh - var(--topbar-height));transition:margin-right 0.3s ease}
.page{display:none;animation:fadeInUp 0.4s ease}.page.active{display:block}
@keyframes fadeInUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.card{background:var(--bg-card);backdrop-filter:blur(15px);border:1px solid var(--border);border-radius:var(--radius);padding:24px;transition:var(--transition);position:relative;overflow:hidden}
.card:hover{transform:translateY(-4px);box-shadow:0 10px 40px rgba(108,92,231,0.15);border-color:rgba(108,92,231,0.4)}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--primary),transparent);opacity:0;transition:opacity 0.3s}
.card:hover::before{opacity:1}
.grid{display:grid;gap:20px}.grid-2{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}.grid-3{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}.grid-4{grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.btn{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:var(--radius-sm);border:none;cursor:pointer;font-family:'Vazirmatn',sans-serif;font-size:14px;font-weight:600;transition:var(--transition);text-decoration:none}
.btn-primary{background:linear-gradient(135deg,var(--primary),#5a4bd1);color:#fff}.btn-primary:hover{transform:translateY(-2px);box-shadow:0 5px 20px rgba(108,92,231,0.4)}
.btn-accent{background:linear-gradient(135deg,var(--accent),#00b3b0);color:#0a0e27}.btn-accent:hover{transform:translateY(-2px)}
.btn-success{background:linear-gradient(135deg,var(--success),#00a884);color:#fff}
.btn-warning{background:linear-gradient(135deg,var(--warning),#f0bf4d);color:#0a0e27}
.btn-danger{background:linear-gradient(135deg,var(--danger),#d4553c);color:#fff}
.btn-outline{background:transparent;border:1px solid var(--border);color:var(--text-secondary)}.btn-outline:hover{border-color:var(--primary);color:var(--primary-light);background:rgba(108,92,231,0.1)}
.btn-sm{padding:6px 14px;font-size:12px}.btn-lg{padding:14px 28px;font-size:16px}.btn-block{width:100%;justify-content:center}
.section-title{font-size:20px;font-weight:700;margin-bottom:20px;display:flex;align-items:center;gap:10px}.section-title .emoji{font-size:24px}
.page-title{font-size:28px;font-weight:900;margin-bottom:8px}.page-subtitle{color:var(--text-secondary);font-size:14px;margin-bottom:24px}
.stat-card{background:var(--bg-card);backdrop-filter:blur(15px);border:1px solid var(--border);border-radius:var(--radius);padding:20px;text-align:center;transition:var(--transition)}
.stat-card:hover{transform:translateY(-4px);box-shadow:0 8px 30px rgba(108,92,231,0.15)}
.stat-icon{font-size:32px;margin-bottom:8px}
.stat-value{font-size:28px;font-weight:900;background:linear-gradient(135deg,var(--primary-light),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-label{font-size:12px;color:var(--text-secondary);margin-top:4px}
.progress-ring{position:relative;width:100px;height:100px;margin:0 auto}
.progress-ring svg{transform:rotate(-90deg)}.progress-ring circle{fill:none;stroke-width:8;stroke-linecap:round}
.progress-ring .bg{stroke:rgba(108,92,231,0.15)}.progress-ring .fg{stroke:var(--primary);transition:stroke-dashoffset 1s ease}
.progress-ring .text{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:18px;font-weight:700}
.flashcard-container{perspective:1000px;width:100%;max-width:400px;height:280px;margin:0 auto}
.flashcard{width:100%;height:100%;position:relative;transform-style:preserve-3d;transition:transform 0.6s cubic-bezier(0.4,0,0.2,1);cursor:pointer}
.flashcard.flipped{transform:rotateY(180deg)}
.flashcard-front,.flashcard-back{position:absolute;width:100%;height:100%;backface-visibility:hidden;border-radius:var(--radius);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:30px;text-align:center}
.flashcard-front{background:linear-gradient(135deg,var(--primary),#5a4bd1)}
.flashcard-back{background:linear-gradient(135deg,var(--accent),#00b3b0);transform:rotateY(180deg);color:#0a0e27}
.chat-container{display:flex;flex-direction:column;height:calc(100vh - var(--topbar-height) - 100px);background:var(--bg-card);border-radius:var(--radius);border:1px solid var(--border);overflow:hidden}
.chat-header{padding:16px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:10px}
.chat-messages{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:12px}
.chat-input-area{padding:16px 20px;border-top:1px solid var(--border);display:flex;gap:10px}
.chat-input{flex:1;background:rgba(108,92,231,0.1);border:1px solid var(--border);border-radius:var(--radius-sm);padding:12px 16px;color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:14px;outline:none;transition:var(--transition)}
.chat-input:focus{border-color:var(--primary)}
.message{max-width:80%;padding:12px 16px;border-radius:16px;font-size:14px;line-height:1.8;animation:fadeInUp 0.3s ease}
.message-bot{background:rgba(108,92,231,0.15);align-self:flex-start;border-bottom-right-radius:4px}
.message-user{background:linear-gradient(135deg,var(--primary),#5a4bd1);align-self:flex-end;border-bottom-left-radius:4px}
.message-time{font-size:11px;color:var(--text-muted);margin-top:4px}
.typing-indicator{display:flex;gap:4px;padding:12px 16px}
.typing-indicator span{width:8px;height:8px;background:var(--text-muted);border-radius:50%;animation:typingBounce 1.4s infinite}
.typing-indicator span:nth-child(2){animation-delay:0.2s}.typing-indicator span:nth-child(3){animation-delay:0.4s}
@keyframes typingBounce{0%,60%,100%{transform:translateY(0)}30%{transform:translateY(-8px)}}
.quick-questions{display:flex;flex-wrap:wrap;gap:8px;padding:10px 20px}
.quick-q{padding:6px 14px;border-radius:20px;background:rgba(108,92,231,0.1);border:1px solid var(--border);color:var(--text-secondary);font-size:12px;cursor:pointer;transition:var(--transition);font-family:'Vazirmatn',sans-serif}
.quick-q:hover{background:rgba(108,92,231,0.2);color:var(--text);border-color:var(--primary)}
.timer-container{text-align:center;padding:40px}
.timer-circle{width:220px;height:220px;margin:0 auto 30px;position:relative}
.timer-circle svg{width:100%;height:100%;transform:rotate(-90deg)}
.timer-circle .bg{fill:none;stroke:rgba(108,92,231,0.15);stroke-width:8}
.timer-circle .fg{fill:none;stroke:var(--primary);stroke-width:8;stroke-linecap:round;transition:stroke-dashoffset 1s linear}
.timer-display{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:42px;font-weight:900}
.timer-label{font-size:14px;color:var(--text-secondary);margin-top:-20px;margin-bottom:20px}
.timer-controls{display:flex;gap:12px;justify-content:center}
.drug-header{padding:16px 20px;display:flex;align-items:center;justify-content:space-between;cursor:pointer}
.drug-body{padding:0 20px 20px;display:none}.drug-card.expanded .drug-body{display:block;animation:fadeIn 0.3s ease}
.drug-category-tag{padding:3px 10px;border-radius:12px;font-size:11px;font-weight:600}
.question-card{border-radius:var(--radius);padding:24px}
.question-text{font-size:16px;font-weight:600;margin-bottom:20px;line-height:1.8}
.option{padding:12px 16px;border:1px solid var(--border);border-radius:var(--radius-sm);margin-bottom:10px;cursor:pointer;transition:var(--transition);display:flex;align-items:center;gap:12px}
.option:hover{border-color:var(--primary);background:rgba(108,92,231,0.1)}
.option.correct{border-color:var(--success);background:rgba(0,184,148,0.1)}
.option.wrong{border-color:var(--danger);background:rgba(225,112,85,0.1)}
.option-letter{width:30px;height:30px;border-radius:50%;background:rgba(108,92,231,0.15);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;flex-shrink:0}
.option.correct .option-letter{background:rgba(0,184,148,0.3)}
.option.wrong .option-letter{background:rgba(225,112,85,0.3)}
.rationale{display:none;padding:16px;background:rgba(0,184,148,0.08);border-radius:var(--radius-sm);margin-top:16px;border:1px solid rgba(0,184,148,0.2)}
.rationale.show{display:block;animation:fadeIn 0.3s ease}
.form-group{margin-bottom:16px}.form-label{display:block;font-size:13px;font-weight:600;color:var(--text-secondary);margin-bottom:6px}
.form-input,.form-select,.form-textarea{width:100%;padding:12px 16px;background:rgba(108,92,231,0.08);border:1px solid var(--border);border-radius:var(--radius-sm);color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:14px;outline:none;transition:var(--transition)}
.form-input:focus,.form-textarea:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(108,92,231,0.1)}
.form-textarea{min-height:100px;resize:vertical}
.form-select{cursor:pointer;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%236c5ce7' d='M6 8L1 3h10z'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:14px center}
.ref-table{width:100%;border-collapse:separate;border-spacing:0}
.ref-table th{background:rgba(108,92,231,0.15);padding:12px 16px;text-align:right;font-size:13px;font-weight:600;color:var(--primary-light)}
.ref-table td{padding:10px 16px;border-bottom:1px solid rgba(108,92,231,0.1);font-size:13px}
.ref-table tr:hover td{background:rgba(108,92,231,0.05)}
.tabs{display:flex;gap:4px;margin-bottom:20px;flex-wrap:wrap}
.tab{padding:8px 16px;border-radius:var(--radius-sm);cursor:pointer;font-size:13px;font-weight:500;color:var(--text-secondary);transition:var(--transition);border:1px solid transparent}
.tab:hover{color:var(--text);background:rgba(108,92,231,0.1)}
.tab.active{background:rgba(108,92,231,0.2);color:var(--primary-light);border-color:var(--border)}
.search-bar{position:relative;margin-bottom:20px}
.search-bar input{width:100%;padding:12px 48px 12px 16px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:14px;outline:none;transition:var(--transition)}
.search-bar input:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(108,92,231,0.1)}
.search-bar .search-icon{position:absolute;left:16px;top:50%;transform:translateY(-50%);color:var(--text-muted)}
.badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:600}
.badge-primary{background:rgba(108,92,231,0.2);color:var(--primary-light)}
.badge-success{background:rgba(0,184,148,0.2);color:var(--success)}
.badge-warning{background:rgba(253,203,110,0.2);color:var(--warning)}
.badge-danger{background:rgba(225,112,85,0.2);color:var(--danger)}
.badge-accent{background:rgba(0,206,201,0.2);color:var(--accent)}
.topic-content{line-height:2;font-size:15px}
.topic-content h3{color:var(--primary-light);margin:20px 0 10px;font-size:17px}
.topic-content ul{padding-right:20px;margin:10px 0}.topic-content li{margin-bottom:8px}
.topic-content .important-note{background:rgba(253,203,110,0.1);border:1px solid rgba(253,203,110,0.3);border-radius:var(--radius-sm);padding:14px 18px;margin:16px 0}
.topic-content .references{background:rgba(108,92,231,0.08);border-radius:var(--radius-sm);padding:14px 18px;margin-top:20px;font-size:13px;color:var(--text-secondary)}
.calendar-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:8px}
.calendar-day{text-align:center}.calendar-day-name{font-size:12px;color:var(--text-muted);margin-bottom:8px;font-weight:600}
.calendar-block{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-sm);min-height:80px;padding:8px;font-size:11px}
.calendar-block.today{border-color:var(--primary)}
.resource-card{text-align:center;padding:30px 20px}.resource-icon{font-size:40px;margin-bottom:12px}.resource-name{font-weight:700;margin-bottom:8px}
.resource-desc{font-size:13px;color:var(--text-secondary);line-height:1.8;margin-bottom:12px}
.modal-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.6);backdrop-filter:blur(5px);z-index:2000;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:var(--transition)}
.modal-overlay.show{opacity:1;visibility:visible}
.modal{background:var(--bg-secondary);border:1px solid var(--border);border-radius:var(--radius);padding:30px;max-width:500px;width:90%;max-height:80vh;overflow-y:auto;transform:scale(0.9);transition:var(--transition)}
.modal-overlay.show .modal{transform:scale(1)}
.toast{position:fixed;bottom:30px;left:50%;transform:translateX(-50%);background:var(--bg-secondary);border:1px solid var(--border);border-radius:var(--radius-sm);padding:12px 24px;z-index:3000;animation:slideUp 0.3s ease;box-shadow:0 10px 30px rgba(0,0,0,0.3)}
@keyframes slideUp{from{transform:translateX(-50%) translateY(20px);opacity:0}to{transform:translateX(-50%) translateY(0);opacity:1}}
@media(max-width:768px){.sidebar{transform:translateX(100%)}.sidebar.open{transform:translateX(0)}.topbar{right:0}.main-content{margin-right:0}.hamburger{display:block}.grid-2,.grid-3,.grid-4{grid-template-columns:1fr}.calendar-grid{grid-template-columns:1fr}.flashcard-container{max-width:100%}}
@media(max-width:480px){.main-content{padding:16px}.stat-value{font-size:22px}.page-title{font-size:22px}}
"""
print("CSS built:", len(css), "chars")
print("SUCCESS - CSS ready")
