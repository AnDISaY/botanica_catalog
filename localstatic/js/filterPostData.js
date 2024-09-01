function createApart(resp) {
  apartments = document.querySelectorAll('.project-apartments__apart');
  apartments.forEach(apart => {apart.remove()});
  notFind = document.querySelector('.notfindtext');
  if (notFind) {
    notFind.remove();
  }

  if (resp['apartmentsf'].length != 0) {
    for (index in resp['apartmentsf']) {
      fields = resp['apartmentsf'][index]['fields'];
  
      apart = document.createElement("div");
      apart.classList.add("project-apartments__apart");
  
      tags = document.createElement("div");
      tags.classList.add("project-apartments__apart__tags");
      tag = document.createElement("div");
      tag.classList.add("project-apartments__apart__tag");
      tag.innerHTML = fields['name']
      tag2 = document.createElement("div");
      tag2.classList.add("project-apartments__apart__tag");
      tag2.innerHTML = fields['description']
      tags.appendChild(tag);
      tags.appendChild(tag2);
      apart.appendChild(tags);
  
      image = document.createElement("div"); 
      image.classList.add('project-apartments__apart__image');
      img = document.createElement("img"); 
      img.src = `/media/${fields['image']}`;
      img.alt = "Apartment image";
      image.appendChild(img);
      apart.appendChild(image);
  
      content = document.createElement("div"); 
      content.classList.add('project-apartments__apart__content');
      row = document.createElement("div"); 
      row.classList.add('project-apartments__apart__row');
      text = document.createElement("div"); 
      text.classList.add('project-apartments__apart__text');
      text.innerHTML = "Тип — GFB";
      text2 = document.createElement("div"); 
      text2.classList.add('project-apartments__apart__text2');
      text2.innerHTML = `${fields['bedroom']} спальни`;
      row.appendChild(text);
      row.appendChild(text2);
      
      row2 = document.createElement("div"); 
      row2.classList.add('project-apartments__apart__row');
      text = document.createElement("div"); 
      text.classList.add('project-apartments__apart__text');
      text.innerHTML = "Площадь";
      text2 = document.createElement("div"); 
      text2.classList.add('project-apartments__apart__text2');
      text2.innerHTML = `${fields['square']} м²`;
      row2.appendChild(text);
      row2.appendChild(text2);
  
      row3 = document.createElement("div"); 
      row3.classList.add('project-apartments__apart__row');
      text = document.createElement("div"); 
      text.classList.add('project-apartments__apart__text');
      text.innerHTML = "Тип — GFB";
      text2 = document.createElement("div"); 
      text2.classList.add('project-apartments__apart__text2');
      text2.innerHTML = `${fields['built_square']} м²`;
      row3.appendChild(text);
      row3.appendChild(text2);
  
      row4 = document.createElement("div"); 
      row4.classList.add('project-apartments__apart__row');
      text = document.createElement("div"); 
      text.classList.add('project-apartments__apart__text');
      text.innerHTML = "Тип — GFB";
      text2 = document.createElement("div"); 
      text2.classList.add('project-apartments__apart__text2');
      text2.innerHTML = `${fields['house_square']} м²`;
      row4.appendChild(text);
      row4.appendChild(text2);
  
  
      content.appendChild(row);
      content.appendChild(row2);
      content.appendChild(row3);
      content.appendChild(row4);
      apart.appendChild(content);
  
      document.querySelector('.project-apartments__wrapper').appendChild(apart);
    }
  } else {
    notFind = document.createElement("span");
    notFind.classList.add('notfindtext')
    notFind.innerHTML = "Нет подходящих вилл";
    document.querySelector('.project-apartments__wrapper').appendChild(notFind);
  }
  
}


$('#my-form').on('submit', function(event) {
  event.preventDefault();
  $.ajax({
    url: window.location.pathname,
    type: 'POST',
    data: $(this).serialize(),
    success: function(resp) {
      createApart(resp);
    }
  });
});


