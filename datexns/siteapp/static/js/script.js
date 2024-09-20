"use strict"

const isMobile = {
	Android: function () {
		return navigator.userAgent.match(/Android/i);
	},
	BlackBerry: function () {
		return navigator.userAgent.match(/BlackBerry/i);
	},
	iOS: function () {
		return navigator.userAgent.match(/iPhone|iPad|iPod/i);
	},
	Opera: function () {
		return navigator.userAgent.match(/Opera Mini/i);
	},
	Windows: function () {
		return navigator.userAgent.match(/IEMobile/i);
	},
	any: function () {
		return (
			isMobile.Android() ||
			isMobile.BlackBerry() ||
			isMobile.iOS() ||
			isMobile.Opera() ||
			isMobile.Windows());
	}
};

if (isMobile.any()){
	document.body.classList.add('_touch');
	let menuArrows = document.querySelectorAll('.menu_arrow' && '.menu_arrow_link');
	if (menuArrows.length>0){
		for (let index = 0; index < menuArrows.length; index++){
			const menuArrow = menuArrows[index];
			menuArrow.addEventListener("click", function (e) {
				menuArrow.parentElement.classList.toggle('_active');
			});
		}
	}
} else {
	document.body.classList.add('_pc');
};

const iconMenu = document.querySelector('.menu_icon');
if(iconMenu){
	const menuBody = document.querySelector('.menu_body');
	iconMenu.addEventListener("click", function(e){
		document.body.classList.toggle('_lock');
		iconMenu.classList.toggle('_active');
		menuBody.classList.toggle('_active');
	});
};


new Swiper('.image-slider',{
	autoHeight:true,
	slidesPerView: 'auto',
	spaceBetween: 60,
	slidesPerGroup: 3,
	loop: true,
	freeMode: true,
	autoplay:{
		delay: 2000,
		disableOnInteraction: false,
	},
	speed: 800,

});
new Swiper('.container_slide',{
	slidesPerView: 'auto',
	loop: true,
	freeMode: true,
	autoplay:{
		delay: 5000,
		disableOnInteraction: false,
	},
	speed: 800,
});