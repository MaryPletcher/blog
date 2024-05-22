// JavaScript to fetch and display blog posts
window.onload = function() {
    fetchPosts();
};

const { exec } = require('child_process');

function fetchPosts() {
    // Fetch the JSON file containing post data
    fetch('posts.json')
        .then(response => response.json())
        .then(posts => displayPosts(posts))
        .catch(error => console.error('Error fetching posts:', error));
}

function displayPosts(posts) {
    const postsContainer = document.getElementById('posts-container');

    posts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.classList.add('post');
        postElement.innerHTML = `
            <h2>${post.title}</h2>
            <p>${post.content}</p>
            <hr>
            <div class = "postFooter">
            <h3 class ="date">${post.date}</h3>
            <img src="media/link.png" alt="Link Icon" class ="link">
            </div>
        `;
        postsContainer.appendChild(postElement);
    });
}
