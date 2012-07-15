$(document).ready(function() {

    //
    // Add New Class
    //
    $("#add_class_button").click(function(e) {
        e.preventDefault();

        var newClass = $("#new_class").val();
        var id = 1234;

        // Add it to our list of classes
        $("#classes").append('<li><span class="label label-success" data-id="' + id + '">' + newClass + '<a class="remove-class" title="Remove" href="#">&times</a></span></li>');

        // Also, add it to our select boxes
        $("#training_classes").append('<option value=' + id + '>' + newClass + '</option>')

        // Reset text box
        $("#new_class").val("");
    });

    //
    // Delete Existing Class
    //
    $(".remove-class").live("click", function(e) {
        e.preventDefault();

        // Find the id
        var id = $(this).parent().attr("data-id");

        // Remove the li
        $(this).parent().remove();

        // Also, remove option from our select boxes
        $("#training_classes option[value='" + id + "']").remove();
    });

    //
    // Add Training Sample
    //
    $("#add_training_sample_button").click(function(e) {
        e.preventDefault();

        var sampleText = $("#training_text").val();
        var sampleClass = $("#training_classes option:selected").val();
        var id = 1234;

        // Add it to our list of samples
        $("#training_samples").append('<li class="outline" data-id=' + id + '>' + sampleText + ' &rarr; ' + sampleClass + '<a class="remove-sample" title="Remove" href="#">&times</a></span></li>');

        // Reset text box
        $("#training_text").val("");

        // Reset select
        $("#training_classes").val("default");
    });

    //
    // Delete Existing Sample
    //
    $(".remove-sample").live("click", function(e) {
        e.preventDefault();

        // Find the id
        var id = $(this).parent().attr("data-id");

        // Remove the li
        $(this).parent().remove();
    });

    //
    // New Classification
    //
    $("#new_classification_button").click(function(e) {
        e.preventDefault();

        var newClassificationText = $("#new_classification_text").val();
        var id = 1234;
        var confidence = 0.98;
        var classification = "FOO";

        // Add it to our list of classifications
        $("#classifications").append('<li class="outline" data-id=' + id + '>' + newClassificationText + ' &rarr; ' + classification + ' (' + confidence + ') <a class="remove-classification" title="Remove" href="#">&times</a></span></li>');

        // Reset text box
        $("#new_classification_text").val("");
    });

    //
    // Delete Existing Classification
    //
    $(".remove-classification").live("click", function(e) {
        e.preventDefault();

        // Find the id
        var id = $(this).parent().attr("data-id");

        // Remove the li
        $(this).parent().remove();
    });

});