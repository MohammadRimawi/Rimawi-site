// ele = null
function next(elm,user=1){
    //  ele = elm.getElementsByClassName("slider")[0];
    var ele = elm
    
    if(user){
        ele = elm.parentElement.getElementsByClassName("slider-body")[0];
        ele.classList.remove("shuffle");
    }

    var offset= ele.scrollWidth/ele.children.length
    var slider = (ele.scrollWidth-ele.scrollLeft)-ele.offsetWidth;
    
    if(ele.scrollLeft+ele.offsetWidth>ele.scrollWidth-15){

        var temp = ele.scrollLeft ;
        
        var card = ele.getElementsByClassName("card")[0]
        // .parentElement;
        ele.getElementsByClassName("card")[0].remove();
        // .parentElement
        ele.append(card);
            
        // ele.scrollLeft= temp-200;
        
        // offset= ele.scrollWidth/ele.children.length
        // slider = (ele.scrollWidth-ele.scrollLeft)-ele.offsetWidth;
        
        ele.scrollLeft-= offset;
        console.log(ele.scrollLeft)
        setTimeout(()=>{

            ele.scroll({
                left: ele.scrollWidth,
                behavior: 'smooth'
            });
            
        },500*!user+user*20);
        return 0;
    }
    

    offset= slider%offset;
    offset+=ele.scrollLeft+1;

    ele.scroll({
        left: offset,
        behavior: 'smooth'
    });
 


}

function previous(elm,user=1){
        
    const ele = elm.parentElement.getElementsByClassName("slider-body")[0];
    console.log(ele)
    if(user){
        ele.classList.remove("shuffle");
    }

    var offset= ele.scrollWidth/ele.children.length
    var slider =ele.scrollWidth-(ele.scrollWidth-ele.scrollLeft);
    
    if(ele.scrollLeft<15){

        var temp = ele.scrollLeft+offset;
        var cards = ele.getElementsByClassName("card");
        var card = cards[cards.length-1];
        ele.getElementsByClassName("card")[cards.length-1].remove();
        ele.prepend(card);

        ele.scrollLeft+= offset;
        
        // offset= ele.scrollWidth/ele.children.length
        // slider =ele.scrollWidth-(ele.scrollWidth-ele.scrollLeft);

        setTimeout(() => {
            ele.scroll({
                left: 0,
                behavior: 'smooth'
                
            });
        }, 20);
         return 0;
        
    }
        offset= slider%offset;
        
        offset=ele.scrollLeft-1 - offset;
        // ele.scrollLeft+= offset;
        setTimeout(()=>{

            ele.scroll({
                left: offset,
                behavior: 'smooth'
            });
            
        },100*user);

}


function load_sliders(){

}
function shuffle(){

    var sliders = document.getElementsByClassName("shuffle");

    for(var i=0;i<sliders.length;i++){5
       sliders[i].scroll({
        left: sliders[i].scrollWidth,
        behavior: 'smooth'
        
    });
    }
    
    setInterval(()=>{
        var sliders = document.getElementsByClassName("shuffle");

        for(var i=0;i<sliders.length;i++){5
            next(sliders[i],0);
        }
        
    },7000);
}


