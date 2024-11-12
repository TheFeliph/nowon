const logoutButton = document.querySelector('.logout-btn');

if (logoutButton) {
    logoutButton.addEventListener('click', (e) => {
        const confirmed = confirm('Você tem certeza que deseja sair?');
        if (!confirmed) {
            e.preventDefault();
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const tweetForm = document.querySelector('.tweet-box form');
    const tweetInput = document.querySelector('.tweet-box textarea');
    const feedContainer = document.querySelector('.feed-content div');

    tweetForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const content = tweetInput.value.trim();
        if (content) {
            fetch('', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: new URLSearchParams({
                    content: content
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.new_post) {
                    
                    const newTweet = document.createElement('div');
                    newTweet.classList.add('tweet');
                    newTweet.innerHTML = `
                        <div class="tweet-content">
                            <div class="tweet-header">
                                <strong>${data.username}</strong>
                            </div>
                            <p>${data.new_post}</p>
                        </div>
                    `;
                    
                    feedContainer.insertBefore(newTweet, feedContainer.firstChild);
                    tweetInput.value = '';
                }
            })
            .catch(error => console.error('Erro ao enviar o tweet:', error));
        }
    });
});