const searchBar = document.querySelector('.search-bar')
const ulLiveSearch = document.getElementById('live-search')
const ingredientsBox = document.querySelector('.selected-ingredients')
const selectedIngredients = document.getElementsByClassName('selected-ingredient-span')
const searchButton = document.querySelector('.search-button')

searchBar.addEventListener('input', inputSearchBar);

function inputSearchBar() {
  let searchInput = this.value
  let ing = {
    ingredient: searchInput,
  };
  if (searchInput) {
    liveSearchFetch(ing)
  } else {
    ulLiveSearch.innerHTML = ''
    ulLiveSearch.style.display = 'none';
  };
};


function liveSearchFetch(ing) {
  fetch('http://127.0.0.1:5000/live-search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(ing)
  })
    .then(response => {
      return response.json();
    })
    .then(data => {
      ulLiveSearch.innerHTML = ''
      if (data.length > 0) {
        ulLiveSearch.style.display = 'block';
      } else {
        ulLiveSearch.style.display = 'none';
      }

      data.forEach(element => {
        let li = document.createElement('li');
        li.innerHTML = element;
        li.className = 'search-element';
        li.addEventListener('click', function () {
          ulLiveSearch.innerHTML = ''
          ulLiveSearch.style.display = 'none';
          searchBar.value = ''

          let span = document.createElement('span');
          span.innerHTML = li.innerHTML;
          span.className = 'selected-ingredient-span';

          let btn = document.createElement('input');
          btn.type = 'button';
          btn.className = 'search-element-btn';

          btn.addEventListener('click', function () {
            span.remove();
          })

          span.appendChild(btn);

          ingredientsBox.appendChild(span);
        });

        ulLiveSearch.appendChild(li);

      });
    })
};


searchButton.addEventListener('click', function () {
  console.log(selectedIngredients);
  let ingList = []
  for (element of selectedIngredients) {
    ingList.push(element.innerText);
  }

  if (ingList.length > 0) {
    window.location.href = `http://127.0.0.1:5000/search/${ingList}`;
  }

});






