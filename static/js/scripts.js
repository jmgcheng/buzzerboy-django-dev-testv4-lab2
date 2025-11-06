document.addEventListener("DOMContentLoaded", function() {
    // 
    console.log("DOM is ready!");

    // 
    setTimeout(function() {
        document.querySelectorAll('.alert').forEach(function(alert) {
        var closeButton = alert.querySelector('[data-bs-dismiss="alert"]');
        if (closeButton) closeButton.click();
        });
    }, 3000);



    // Global delete modal handler
    document.addEventListener('DOMContentLoaded', function() {
        const deleteModal = $('#confirmDeleteModal');
        const deleteForm = document.getElementById('deleteForm');
        const deleteMessage = document.getElementById('deleteModalMessage');

        // Attach to any delete button
        document.body.addEventListener('click', function(e) {
        const btn = e.target.closest('[data-toggle="delete-modal"]');
        if (btn) {
            const url = btn.getAttribute('data-url');
            const itemName = btn.getAttribute('data-item') || 'this item';

            // Update modal content dynamically
            deleteForm.action = url;
            deleteMessage.textContent = `Are you sure you want to delete ${itemName}?`;

            // Open modal
            deleteModal.modal('show');
        }
        });
    });




});