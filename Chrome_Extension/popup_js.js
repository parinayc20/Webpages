document.addEventListener('DOMContentLoaded',function (){
    document.querySelector('button').addEventListener('click',video_rate);
    function video_rate(){
        var c=document.getElementById('video_rate').value;
        chrome.tabs.query({currentWindow: true, active: true},
        function (tabs){
            chrome.tabs.sendMessage(tabs[0].id,c);
        });
    }
});