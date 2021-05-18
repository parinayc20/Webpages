// alert('HI');
// console.log('hi');
chrome.runtime.onMessage.addListener(function (query){
    var c=document.getElementsByTagName("video");
    console.log(' '+c.length+' ');
    if(query<0.07 || query>16){
        alert('Invalid Rate\nInput a rate between 0.07-16.0');
    }
    else
    if(c.length === 0){
        alert('No Active Videos');
    }
    else
    {
        for(var i=0;i<c.length;i++){
            c[i].playbackRate=query;
        }
    }
});