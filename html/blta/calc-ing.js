

function calcIng(){
    var numsand = document.getElementById("sandwichnum").value;
    
    var numleaves = numsand*2;
    var numbunch = Math.ceil(numleaves/16); //assuming 16 leaves per bunch
    var numbread = numsand*2;
    var numloaves = Math.ceil(numbread/24);  //assuming 24 slices per loaf
    var numstrips = numsand*3;
    var numpack = Math.ceil(numstrips/18); //assuming 18 strips of bacon per package
    var numwedge = numsand*4;
    var numtomato = Math.ceil(numwedge/16); // assuming 16 wedges per tomato
    var numhalf = numsand;
    var numavocado = Math.ceil(numhalf/2); // 2 halves per avocado
    
    document.getElementById("breadslices").value = numbread.toString();
    document.getElementById("bread").value = numloaves.toString();
    document.getElementById("baconstrips").value = numstrips.toString();
    document.getElementById("baconpack").value = numpack.toString();
    document.getElementById("lettuceleaf").value = numleaves.toString();
    document.getElementById("lettucehead").value = numbunch.toString();
    document.getElementById("tomatowedge").value = numwedge.toString();
    document.getElementById("tomato").value = numtomato.toString();
    document.getElementById("avocadohalves").value = numhalf.toString();
    document.getElementById("avocados").value = numavocado.toString();
    
    
}