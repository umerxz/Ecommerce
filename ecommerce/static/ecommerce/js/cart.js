var updateButtons=document.getElementsByClassName('update-cart')

for(var i=0;i<updateButtons.length;i++){

  updateButtons[i].addEventListener('click', function(){
    var productId=this.dataset.product
    var action=this.dataset.action
    console.log('productId: ',productId)
    console.log('action: ',action)
    updateOrder(action,productId)
  })
}

function updateOrder(action,productId){
  console.log('IN FUNC')

  var url='/update_order/'
  fetch(url,{
    method:'POST',
    headers:{
      'Content-Type': 'application/json',
      'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'productId':productId,'action':action})
  })
  .then((response)=>{
    return response.json
  })
  .then((data) =>{
    console.log('data',data)
    location.reload()
  } )
}
