// Custom JavaScript for Student Result Management System

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('form[onsubmit*="confirm"]');
    deleteButtons.forEach(button => {
        button.addEventListener('submit', function(e) {
            const confirmed = confirm('Are you sure you want to delete this item?');
            if (!confirmed) {
                e.preventDefault();
            }
        });
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Auto-hide top notifications after 3 seconds
    const topNotifications = document.querySelectorAll('.position-fixed.top-0');
    topNotifications.forEach(notification => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(notification);
            bsAlert.close();
        }, 3000);
    });

    // Search functionality with debounce
    const searchInputs = document.querySelectorAll('input[name="search"]');
    searchInputs.forEach(input => {
        let timeout;
        input.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                // Auto-submit search form
                const form = input.closest('form');
                if (form) {
                    form.submit();
                }
            }, 500);
        });
    });

    // Form validation feedback
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Dynamic grade color coding
    const gradeBadges = document.querySelectorAll('.badge');
    gradeBadges.forEach(badge => {
        const grade = badge.textContent.trim();
        switch(grade) {
            case 'A':
                badge.classList.add('bg-success');
                break;
            case 'B':
                badge.classList.add('bg-primary');
                break;
            case 'C':
                badge.classList.add('bg-warning', 'text-dark');
                break;
            case 'D':
            case 'F':
                badge.classList.add('bg-danger');
                break;
        }
    });

    // Table row hover effects
    const tableRows = document.querySelectorAll('tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f8f9fa';
        });
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
        });
    });

    // Pagination active state
    const currentPage = new URLSearchParams(window.location.search).get('page') || 1;
    const pageLinks = document.querySelectorAll('.pagination .page-link');
    pageLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href && href.includes(`page=${currentPage}`)) {
            link.closest('.page-item').classList.add('active');
        }
    });

    // Loading state for forms
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(button => {
        button.closest('form').addEventListener('submit', function() {
            button.disabled = true;
            button.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Processing...';
        });
    });

    // Date picker initialization (if using date inputs)
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(input => {
        // Set max date to today for exam dates
        if (input.name === 'exam_date') {
            input.max = new Date().toISOString().split('T')[0];
        }
    });

    // Score validation
    const scoreInputs = document.querySelectorAll('input[name="score"]');
    scoreInputs.forEach(input => {
        input.addEventListener('input', function() {
            const value = parseFloat(this.value);
            if (value < 0 || value > 100) {
                this.setCustomValidity('Score must be between 0 and 100');
            } else {
                this.setCustomValidity('');
            }
        });
    });

    // Auto-calculate grade based on score (optional feature)
    const scoreInput = document.querySelector('input[name="score"]');
    const gradeSelect = document.querySelector('select[name="grade"]');
    if (scoreInput && gradeSelect) {
        scoreInput.addEventListener('input', function() {
            const score = parseFloat(this.value);
            let suggestedGrade = '';
            if (score >= 90) suggestedGrade = 'A';
            else if (score >= 80) suggestedGrade = 'B';
            else if (score >= 70) suggestedGrade = 'C';
            else if (score >= 60) suggestedGrade = 'D';
            else if (score >= 0) suggestedGrade = 'F';

            // Only auto-select if no grade is manually selected
            if (suggestedGrade && !gradeSelect.value) {
                gradeSelect.value = suggestedGrade;
            }
        });
    }
});
