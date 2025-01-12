var exampleModal = document.getElementById('addMealsModal')
exampleModal.addEventListener('show.bs.modal', function (event) {
  var button = event.relatedTarget
  var dish_id = button.getAttribute('data-bs-whatever')
  var dish = button.parentNode.querySelector('.card-title').textContent
  var modalTitle = exampleModal.querySelector('.modal-title')
  var modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = 'Добавить блюдо ' + dish
  modalBodyInput.value = dish_id
})