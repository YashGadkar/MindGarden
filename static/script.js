// MindGarden Client-Side Script
// Comprehensive fixes for Chat, Modals, Sliders, Responsiveness, and Notifications

// Global HTML sanitization helper for safe DOM injection
window.escapeHtml = function(str) {
    if (!str && str !== 0) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
};

// Global Toast Notification Helper
window.showToast = function(message, type = "info", duration = 4000) {
    let container = document.querySelector(".toast-container");
    if (!container) {
        container = document.createElement("div");
        container.className = "toast-container";
        document.body.appendChild(container);
    }

    const toast = document.createElement("div");
    toast.className = `toast-item toast-${type}`;
    
    let iconHtml = `<i class="fa-solid fa-circle-info" style="color: #2563eb; font-size: 16px;"></i>`;
    if (type === "success") iconHtml = `<i class="fa-solid fa-circle-check" style="color: #16a34a; font-size: 16px;"></i>`;
    if (type === "error") iconHtml = `<i class="fa-solid fa-triangle-exclamation" style="color: #dc2626; font-size: 16px;"></i>`;

    toast.innerHTML = `
        <div style="display: flex; align-items: center; gap: 10px;">
            <span>${iconHtml}</span>
            <span>${window.escapeHtml(message)}</span>
        </div>
        <button type="button" class="toast-close" aria-label="Close notification">&times;</button>
    `;

    toast.querySelector(".toast-close").addEventListener("click", () => {
        toast.style.opacity = "0";
        toast.style.transform = "translateX(50px)";
        setTimeout(() => toast.remove(), 250);
    });

    container.appendChild(toast);

    setTimeout(() => {
        if (toast.parentElement) {
            toast.style.opacity = "0";
            toast.style.transform = "translateX(50px)";
            setTimeout(() => toast.remove(), 250);
        }
    }, duration);
};

document.addEventListener("DOMContentLoaded", () => {
    // =========================================================================
    // 1. DYNAMIC SLIDER VALUE & FILL PROGRESS DISPLAY (Accessible Contrast)
    // =========================================================================
    const sliders = document.querySelectorAll(".slider-input");
    sliders.forEach(slider => {
        const container = slider.closest(".slider-container");
        if (!container) return;
        const valSpan = container.querySelector(".slider-val");
        if (!valSpan) return;

        const unit = slider.dataset.unit || "";
        const max = slider.max || 10;

        function updateSliderDisplay(val) {
            if (unit === "hrs" || unit === "hours") {
                valSpan.textContent = `${val} ${val == 1 ? "hr" : "hrs"}`;
            } else if (unit) {
                valSpan.textContent = `${val} ${unit}`;
            } else {
                valSpan.textContent = `${val} / ${max}`;
            }
            const min = parseFloat(slider.min) || 0;
            const maxVal = parseFloat(max) || 10;
            const pct = Math.min(100, Math.max(0, ((parseFloat(val) - min) / (maxVal - min)) * 100));
            slider.style.background = `linear-gradient(to right, #15803d 0%, #15803d ${pct}%, #e2e8f0 ${pct}%, #e2e8f0 100%)`;
        }

        updateSliderDisplay(slider.value);
        slider.addEventListener("input", (e) => updateSliderDisplay(e.target.value));
    });

    // =========================================================================
    // 2. NON-DESTRUCTIVE CHAT ENGINE & SMART SCROLL (Fix #1, Fix #3, Fix #4)
    // =========================================================================
    const chatHistory = document.getElementById("chat-history");
    const activeChatPartner = document.getElementById("active-chat-partner");
    const chatReceiverInput = document.getElementById("chat-receiver-id");
    const chatForm = document.getElementById("chat-form");
    const chatInput = document.getElementById("chat-input");
    const chatSendBtn = chatForm ? chatForm.querySelector("button[type='submit']") : null;
    const userItems = document.querySelectorAll(".user-item");
    const counsellorSelectDropdown = document.getElementById("counsellor-chat-select");

    let currentPartnerId = null;
    let lastRenderedMessageCount = 0;
    let isFetchingChat = false;

    window.loadChatHistory = function(partnerId, forceScroll = false) {
        if (!chatHistory || !partnerId || isFetchingChat) return;
        isFetchingChat = true;

        fetch(`/chat/history/${partnerId}`)
            .then(res => res.json())
            .then(messages => {
                isFetchingChat = false;
                if (!Array.isArray(messages)) return;

                // Detect if partner switched
                const isPartnerSwitched = currentPartnerId !== partnerId;
                currentPartnerId = partnerId;

                // Check if user is currently scrolled up reading past history
                const isNearBottom = chatHistory.scrollHeight - chatHistory.scrollTop - chatHistory.clientHeight < 70;

                // If partner switched or message count changed, re-render
                if (isPartnerSwitched || messages.length !== lastRenderedMessageCount) {
                    chatHistory.innerHTML = "";

                    if (messages.length === 0) {
                        chatHistory.innerHTML = `
                            <p style="color: var(--color-slate); text-align: center; margin-top: 35%;">
                                No messages yet. Say hello to start the conversation! 🌱
                            </p>
                        `;
                    } else {
                        messages.forEach(msg => {
                            const msgDiv = document.createElement("div");
                            msgDiv.className = `chat-message ${msg.sent ? 'message-sent' : 'message-received'}`;
                            
                            const textSpan = document.createElement("span");
                            textSpan.textContent = msg.text;
                            msgDiv.appendChild(textSpan);

                            if (msg.time) {
                                const timeSpan = document.createElement("span");
                                timeSpan.className = "message-time";
                                timeSpan.textContent = msg.time;
                                msgDiv.appendChild(timeSpan);
                            }

                            chatHistory.appendChild(msgDiv);
                        });
                    }

                    lastRenderedMessageCount = messages.length;

                    // Only scroll to bottom if forced or if user was already near bottom
                    if (forceScroll || isPartnerSwitched || isNearBottom) {
                        chatHistory.scrollTop = chatHistory.scrollHeight;
                    }
                }
            })
            .catch(err => {
                isFetchingChat = false;
                console.error("Error loading chat history:", err);
            });
    };

    // Counsellor selector in student dashboard chat header (Fix #4)
    if (counsellorSelectDropdown) {
        counsellorSelectDropdown.addEventListener("change", (e) => {
            const partnerId = e.target.value;
            const partnerName = e.target.options[e.target.selectedIndex].text;
            if (chatReceiverInput) chatReceiverInput.value = partnerId;
            if (activeChatPartner) activeChatPartner.textContent = partnerName;
            if (chatInput) chatInput.disabled = false;
            if (chatSendBtn) chatSendBtn.disabled = false;
            window.loadChatHistory(partnerId, true);
        });
    }

    // Counsellor dashboard user item selection
    userItems.forEach(item => {
        item.addEventListener("click", () => {
            const partnerId = item.dataset.userId;
            const partnerName = item.dataset.userName;
            
            userItems.forEach(i => i.classList.remove("active"));
            item.classList.add("active");

            if (activeChatPartner) activeChatPartner.textContent = partnerName;
            if (chatReceiverInput) chatReceiverInput.value = partnerId;
            if (chatInput) chatInput.disabled = false;
            if (chatSendBtn) chatSendBtn.disabled = false;

            window.loadChatHistory(partnerId, true);
        });
    });

    // Initial chat load on page load (Fix #3)
    if (chatReceiverInput && chatReceiverInput.value) {
        window.loadChatHistory(chatReceiverInput.value, true);
    }

    // Async message sending
    if (chatForm && chatInput && chatReceiverInput) {
        chatForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const text = chatInput.value.trim();
            const receiverId = chatReceiverInput.value;

            if (!text || !receiverId) return;

            // Anti-spam disable
            if (chatSendBtn) {
                chatSendBtn.disabled = true;
                chatSendBtn.style.opacity = "0.7";
            }

            fetch("/chat/send", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ receiver_id: receiverId, message: text })
            })
            .then(res => res.json())
            .then(data => {
                if (chatSendBtn) {
                    chatSendBtn.disabled = false;
                    chatSendBtn.style.opacity = "1";
                }

                if (data.status === "success") {
                    // Check if chat-history had empty state
                    const emptyPlaceholder = chatHistory.querySelector("p");
                    if (emptyPlaceholder) emptyPlaceholder.remove();

                    // Append message locally immediately
                    const msgDiv = document.createElement("div");
                    msgDiv.className = "chat-message message-sent";
                    
                    const textSpan = document.createElement("span");
                    textSpan.textContent = text;
                    msgDiv.appendChild(textSpan);

                    const timeSpan = document.createElement("span");
                    timeSpan.className = "message-time";
                    const now = new Date();
                    const hours = String(now.getHours()).padStart(2, "0");
                    const mins = String(now.getMinutes()).padStart(2, "0");
                    timeSpan.textContent = `${hours}:${mins}`;
                    msgDiv.appendChild(timeSpan);

                    chatHistory.appendChild(msgDiv);
                    chatHistory.scrollTop = chatHistory.scrollHeight;
                    chatInput.value = "";
                    lastRenderedMessageCount += 1;
                } else {
                    window.showToast(data.message || "Failed to deliver message.", "error");
                }
            })
            .catch(err => {
                if (chatSendBtn) {
                    chatSendBtn.disabled = false;
                    chatSendBtn.style.opacity = "1";
                }
                console.error("Error sending message:", err);
                window.showToast("Network error sending message. Please try again.", "error");
            });
        });
    }

    // Periodically poll chat non-destructively without hijacking scroll (Fix #1)
    setInterval(() => {
        if (chatReceiverInput && chatReceiverInput.value) {
            window.loadChatHistory(chatReceiverInput.value, false);
        }
    }, 4500);

    // =========================================================================
    // 3. UNIVERSAL MODAL CONTROLLER & CLICK-OUTSIDE / ESCAPE (Fix #7)
    // =========================================================================
    const bookingBtn = document.getElementById("booking-btn");
    const bookingModal = document.getElementById("booking-modal");

    if (bookingBtn && bookingModal) {
        bookingBtn.addEventListener("click", () => {
            bookingModal.style.display = "flex";
        });
    }

    // Close on clicking any close icon (.modal-close)
    document.querySelectorAll(".modal-close").forEach(closeBtn => {
        closeBtn.addEventListener("click", (e) => {
            const parentModal = e.target.closest(".modal-overlay");
            if (parentModal) {
                parentModal.style.display = "none";
            }
        });
    });

    // Close any modal on clicking backdrop
    document.querySelectorAll(".modal-overlay").forEach(overlay => {
        overlay.addEventListener("click", (e) => {
            if (e.target === overlay) {
                overlay.style.display = "none";
            }
        });
    });

    // Close any modal on pressing Escape key
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            document.querySelectorAll(".modal-overlay").forEach(m => {
                m.style.display = "none";
            });
        }
    });

    // =========================================================================
    // 4. MOBILE DRAWER NAVIGATION (Fix #8)
    // =========================================================================
    const hamburgerBtn = document.getElementById("hamburger-btn");
    const sidebar = document.querySelector(".sidebar");
    const sidebarBackdrop = document.getElementById("sidebar-backdrop");

    if (hamburgerBtn && sidebar) {
        hamburgerBtn.addEventListener("click", () => {
            sidebar.classList.toggle("open");
            if (sidebarBackdrop) sidebarBackdrop.classList.toggle("active");
        });
    }

    if (sidebarBackdrop && sidebar) {
        sidebarBackdrop.addEventListener("click", () => {
            sidebar.classList.remove("open");
            sidebarBackdrop.classList.remove("active");
        });
    }

    // Close drawer upon clicking any sidebar navigation link on mobile
    document.querySelectorAll(".sidebar .nav-links a").forEach(link => {
        link.addEventListener("click", () => {
            if (window.innerWidth <= 768 && sidebar) {
                sidebar.classList.remove("open");
                if (sidebarBackdrop) sidebarBackdrop.classList.remove("active");
            }
        });
    });

    // =========================================================================
    // 5. DEMO CREDENTIAL AUTOFILL & PASSWORD TOGGLE (Fix #21)
    // =========================================================================
    document.querySelectorAll("[data-autofill-email]").forEach(btn => {
        btn.addEventListener("click", () => {
            if (typeof toggleAuthView === "function") {
                toggleAuthView("login");
            }
            const emailInput = document.getElementById("login-email");
            const passInput = document.getElementById("login-password");
            const roleSelect = document.getElementById("login-role");

            if (emailInput) emailInput.value = btn.dataset.autofillEmail || "";
            if (passInput) passInput.value = btn.dataset.autofillPass || "";
            if (roleSelect && btn.dataset.autofillRole) roleSelect.value = btn.dataset.autofillRole;

            window.showToast(`Filled credentials for ${btn.textContent.trim()}`, "info", 2000);
        });
    });

    // Toggle password visibility
    document.querySelectorAll(".toggle-password-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const targetId = btn.dataset.targetInput;
            const input = document.getElementById(targetId);
            if (!input) return;

            const icon = btn.querySelector("i");
            if (input.type === "password") {
                input.type = "text";
                if (icon) {
                    icon.classList.remove("fa-eye");
                    icon.classList.add("fa-eye-slash");
                } else {
                    btn.textContent = "🙈";
                }
                btn.title = "Hide password";
            } else {
                input.type = "password";
                if (icon) {
                    icon.classList.remove("fa-eye-slash");
                    icon.classList.add("fa-eye");
                } else {
                    btn.textContent = "👁️";
                }
                btn.title = "Show password";
            }
        });
    });

    // =========================================================================
    // 6. DYNAMIC AJAX CHECKIN HANDLER (/student/checkin)
    // =========================================================================
    const checkinForm = document.getElementById("checkin-form");
    if (checkinForm) {
        checkinForm.addEventListener("submit", (e) => window.submitCheckin(e));
    }
});

// Global AJAX Check-in Handler for /student/checkin
window.submitCheckin = function(event) {
    if (event) event.preventDefault();
    const form = document.getElementById("checkin-form");
    const submitBtn = document.getElementById("submit-checkin-btn");
    if (!form) return;
    const formData = new FormData(form);

    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Analyzing with AI...";
        submitBtn.style.opacity = "0.7";
    }

    fetch("/student/checkin", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "success") {
            const card = document.getElementById("checkin-card");
            if (card) {
                card.innerHTML = `
                    <div class="card-title">
                        <span style="font-size: 24px;">📝</span> Daily Check-in
                    </div>
                    <div style="text-align: center; padding: 24px; animation: bouncePop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);">
                        <span style="font-size: 48px;">🌟</span>
                        <h3 style="margin-top: 16px; color: var(--color-deep-ink);">Check-in successful!</h3>
                        <p style="color: var(--color-slate); margin-top: 8px;">Model classification: <strong>${window.escapeHtml(data.predicted_risk)} Risk</strong></p>
                        <p style="font-size: 13px; color: var(--color-moss-green); margin-top: 4px; font-weight: 600;">Your wellness log and trendlines have been updated below.</p>
                    </div>
                `;
            }

            const tbody = document.getElementById("checkin-history-tbody");
            const noLogsRow = document.getElementById("no-logs-row");
            if (noLogsRow) noLogsRow.remove();

            const log = data.log;
            if (tbody && log) {
                const newRow = document.createElement("tr");
                newRow.style.animation = "bouncePop 0.4s ease";
                newRow.innerHTML = `
                    <td><strong>${window.escapeHtml(log.date)}</strong></td>
                    <td>${window.escapeHtml(log.sleep_hours)} hrs</td>
                    <td>${window.escapeHtml(log.study_hours)} hrs</td>
                    <td>${window.escapeHtml(log.mood_score)}/10</td>
                    <td>
                        <span class="badge-priority badge-${window.escapeHtml(log.predicted_risk.toLowerCase())}">
                            ${window.escapeHtml(log.predicted_risk)}
                        </span>
                    </td>
                `;
                tbody.insertBefore(newRow, tbody.firstChild);
            }

            if (window.healthChart) {
                window.healthChart.data.labels.push(log.date.slice(5));
                window.healthChart.data.datasets[0].data.push(log.sleep_hours);
                window.healthChart.data.datasets[1].data.push(log.study_hours);
                window.healthChart.data.datasets[2].data.push(log.mood_score);
                window.healthChart.update();
            }

            window.showToast(`Daily log recorded! AI Risk: ${data.predicted_risk}`, "success");
        } else {
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.textContent = "Submit Daily Log";
                submitBtn.style.opacity = "1";
            }
            window.showToast(data.message || "Failed to submit checkin.", "error");
        }
    })
    .catch(err => {
        console.error("Error submitting checkin:", err);
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = "Submit Daily Log";
            submitBtn.style.opacity = "1";
        }
        window.showToast("Network error submitting checkin.", "error");
    });
};

