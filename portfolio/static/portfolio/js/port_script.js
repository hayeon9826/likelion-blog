//여기가 바로 연동됨. static 말고  portfolio/static 이 우선


// Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var image = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

image.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
};

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}

// $('#close').click(function(){
//   $('.modal').modal("hide");
// })
var close = document.getElementById("Close");

close.onclick = function(){
  modal.style.display = "none";
}
