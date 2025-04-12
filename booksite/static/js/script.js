const bookContainers = [...document.querySelectorAll('.book-container')];
const preBtn = [...document.querySelectorAll('.pre-btn')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];

bookContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

})

document.querySelectorAll('.show-info-btn').forEach(button => {
  button.addEventListener('click', (e) => {
    const bookCard = e.target.closest('.book-card');
    const info = bookCard.querySelector('.book-info');
    info.classList.remove('hidden'); // show it
  });
});

document.querySelectorAll('.close-btn').forEach(button => {
  button.addEventListener('click', (e) => {
    const bookCard = e.target.closest('.book-card');
    const info = bookCard.querySelector('.book-info');
    info.classList.add('hidden');
  });
});