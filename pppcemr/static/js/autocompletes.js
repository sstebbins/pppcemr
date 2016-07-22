$(function() {
    $("#id_patient").autocomplete({
        source: "/pppcemr/api/get_patient/",
        minLength: 2,
        select: function(event, ui) {
            $("#patient_pk").val(ui.item.id);
            },
//        focus: function(event, ui) {
//            $("#patient_pk").val(ui.item.id);
//            }
    });
});

$(function() {
    $("#id_diagnosis").autocomplete({
        source: "/pppcemr/api/get_diagnosis/",
        minLength: 2,
        select: function(event, ui) {
            $("#diagnosis_pk").val(ui.item.id);
            },
//        focus: function(event, ui) {
//            $("#diagnosis_pk").val(ui.item.id);
//            }
    });
});

$(function() {
    $("#id_treatment_option").autocomplete({
        source: "/pppcemr/api/get_treatment_option/",
        minLength: 2,
        select: function(event, ui) {
            $("#treatment_option_pk").val(ui.item.id);
            },
//        focus: function(event, ui) {
//            $("#treatment_option_pk").val(ui.item.id);
//            }
    });
});

$(function() {
    $("#id_snomed").autocomplete({
        source: "/pppcemr/api/get_snomed/",
        minLength: 2,
        select: function(event, ui) {
            $("#snomed_pk").val(ui.item.id);
            },
//        focus: function(event, ui) {
//            $("#diagnosis_pk").val(ui.item.id);
//            }
    });
});

$(function() {
    $("#id_standard_PE_results").autocomplete({
        source: "/pppcemr/api/get_standard_PE_results/",
        minLength: 1,
        select: function(event, ui) {
            $("#id_PE_constitutional").val(ui.item.PE_constitutional);
            $("#id_PE_head_and_face").val(ui.item.PE_head_and_face);
            $("#id_PE_eyes").val(ui.item.PE_eyes);
            $("#id_PE_ears").val(ui.item.PE_ears);
            $("#id_PE_nose_mouth_and_throat").val(ui.item.PE_nose_mouth_and_throat);
            $("#id_PE_neck").val(ui.item.PE_neck);
            $("#id_PE_chest_and_breast").val(ui.item.PE_chest_and_breast);
            $("#id_PE_respiratory").val(ui.item.PE_respiratory);
            $("#id_PE_heart").val(ui.item.PE_heart);
            $("#id_PE_pulses_vascular").val(ui.item.PE_pulses_vascular);
            $("#id_PE_gastrointestinal").val(ui.item.PE_gastrointestinal);
            $("#id_PE_GU").val(ui.item.PE_GU);
            $("#id_PE_musculoskeletal").val(ui.item.PE_musculoskeletal);
            $("#id_PE_skin_and_nodes").val(ui.item.PE_skin_and_nodes);
            $("#id_PE_neurologic").val(ui.item.PE_neurologic);
            $("#id_PE_psyche").val(ui.item.PE_psyche);
            },
//        focus: function(event, ui) {
//            $("#treatment_option_pk").val(ui.item.id);
//            }
    });
});
