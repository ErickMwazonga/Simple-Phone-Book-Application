$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-contact").modal("show");
      },
      success: function (data) {
        $("#modal-contact .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#contact-table tbody").html(data.html_contact_list);
          $("#modal-contact").modal("hide");
        }
        else {
          $("#modal-contact .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  /* Binding */
  // Create contact
  $(".js-create-contact").click(loadForm);
  $("#modal-contact").on("submit", ".js-contact-create-form", saveForm);
  // Update contact
  $("#contact-table").on("click", ".js-update-contact", loadForm);
  $("#modal-contact").on("submit", ".js-contact-update-form", saveForm);
  // Delete contact
  $("#contact-table").on("click", ".js-delete-contact", loadForm);
  $("#modal-contact").on("submit", ".js-contact-delete-form", saveForm);
});
