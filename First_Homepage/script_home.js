function changeActive(id){
    var target_1=document.getElementById("activated_nav");
    var target_2=document.getElementById(id);
    target_1.removeAttribute('aria-current');
    target_1.setAttribute('id',id);
    target_1.setAttribute('class','nav-link');
    target_2.setAttribute('class','nav-link active');
    target_2.setAttribute('id','activated_nav');
    target_2.setAttribute('aria-current','page');
}
function toggler(){
    var active=document.getElementById("act");
    var inactive=document.getElementById("nact");
    active.setAttribute('class','btn btn-danger btn-lg text-nowrap');
    active.setAttribute('id','nact');
    inactive.setAttribute('class','btn btn-success btn-lg text-nowrap');
    inactive.setAttribute('id','act');
    var active_icon=document.getElementById("act_icon");
    var inactive_icon=document.getElementById("nact_icon");
    active_icon.setAttribute('class','bi bi-plus icon1');
    active_icon.setAttribute('id','nact_icon');
    inactive_icon.setAttribute('class','bi bi-dash icon1');
    inactive_icon.setAttribute('id','act_icon');
}