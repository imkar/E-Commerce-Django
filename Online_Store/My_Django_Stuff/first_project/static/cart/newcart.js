$(document).ready(function () {
  $('.stepper').mdbStepper();
  })

$(document).ready(function () {
  var navListItems = $('div.setup-panel div a'),
      allWells = $('.setup-content'),
      allNextBtn = $('.nextBtn'),
      allPrevBtn = $('.prevBtn');

  allWells.hide();

  navListItems.click(function (e) {
      e.preventDefault();
      var $target = $($(this).attr('href')),
          $item = $(this);

      if (!$item.hasClass('disabled')) {
          navListItems.removeClass('step-button-active').addClass('step-button');
          $item.addClass('step-button-active');
          allWells.hide();
          $target.show();
          $target.find('input:eq(0)').focus();
      }
  });

  allPrevBtn.click(function(){
      var curStep = $(this).closest(".setup-content"),
          curStepBtn = curStep.attr("id"),
          prevStepSteps = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().prev().children("a");

          prevStepSteps.removeAttr('disabled').trigger('click');
  });

  allNextBtn.click(function(){
      var curStep = $(this).closest(".setup-content"),
          curStepBtn = curStep.attr("id"),
          nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),
          curInputs = curStep.find("input[type='text'],input[type='url']"),
          isValid = true;

      $(".form-group").removeClass("has-error");
      for(var i=0; i< curInputs.length; i++){
          if (!curInputs[i].validity.valid){
              isValid = false;
              $(curInputs[i]).closest(".form-group").addClass("has-error");
          }
      }

      if (isValid)
          nextStepWizard.removeAttr('disabled').trigger('click');
  });

  $('div.setup-panel div a.step-button-active').trigger('click');
});
