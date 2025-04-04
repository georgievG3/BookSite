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