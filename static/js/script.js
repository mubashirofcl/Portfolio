
/*======================================================
                        cursor effect
  ======================================================*/


/*======================================================
                        preloader
  ======================================================*/

var loader = document.getElementById("preloader");

window.addEventListener('load', function () {
    loader.style.display = "none";
})

/*======================================================
                        FADE IN ANIMATION
  ======================================================*/

AOS.init({
    duration: 1200,
})


/*======================================================
                        Audio player
  ======================================================*/
function pauseMusic() {

    var audioPlayer = document.getElementById('audio-player');
    var audioContainer = $('#music-container');

    audioPlayer.pause();
    audioContainer.addClass("music-player--disabled");

    console.log("pause music");
}

function playMusic() {

    var audioPlayer = document.getElementById('audio-player');
    var audioContainer = $('#music-container');

    audioPlayer.play();
    audioContainer.removeClass("music-player--disabled");

    console.log("play music");
}

/*======================================================
                      rotative logo
  ======================================================*/
const text = document.querySelector(".text");
text.innerHTML = text.innerText
    .split("")
    .map(
        (char, i) => `<span style="transform:rotate(${i * 10.3}deg)">${char}</span>`
    )
    .join("");


/* client slider */

var copy = document.querySelector(".logos-slide").cloneNode(true);
document.querySelector(".logos").appendChild(copy);

/*  */

document.getElementById("video").muted = true;