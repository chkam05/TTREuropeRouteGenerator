function checkGameExists() {
    fetch(GAME_EXISTS_ENDPOINT)
        .then(response => response.json())
        .then(data => {
            if (!data.game_exists) {
                if (data.summary_exists) {
                    window.location.href = data.summary_route;
                } else {
                    window.location.href = data.home_route;
                }
            } else if (data.should_refresh) {
                window.location.reload();
            }
        })
        .catch(() => {
            window.location.href = '/';
        });
}

setInterval(checkGameExists, 5000);