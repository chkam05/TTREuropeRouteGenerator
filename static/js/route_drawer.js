window.addEventListener('load', () => {
    const image = document.getElementById('map-image-js');
    const canvas = document.getElementById('route-canvas');
    const ctx = canvas.getContext('2d');

    // Wait for the image to load and then set the canvas size.
    image.onload = () => {
        canvas.width = image.naturalWidth;
        canvas.height = image.naturalHeight;
        canvas.style.width = image.clientWidth + 'px';
        canvas.style.height = image.clientHeight + 'px';

        drawRoutes();
    };

    function drawPin(x, y, color = '#e0cfa0', strokeColor = 'black') {
        const ctx = canvas.getContext('2d');
        const pinHeight = 38;
        const pinWidth = 32;
        const holeRadius = 6;

        ctx.save();
        ctx.translate(x, y);

        // --- Pin ---
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.bezierCurveTo(pinWidth / 2, -pinHeight / 3, pinWidth / 2, -pinHeight, 0, -pinHeight);
        ctx.bezierCurveTo(-pinWidth / 2, -pinHeight, -pinWidth / 2, -pinHeight / 3, 0, 0);
        ctx.closePath();

        ctx.fillStyle = color;
        ctx.fill();

        ctx.lineWidth = 1.5;
        ctx.strokeStyle = strokeColor;
        ctx.stroke();

        // --- Hole ---
        ctx.beginPath();
        ctx.arc(0, -pinHeight * 0.6, holeRadius, 0, Math.PI * 2);

        ctx.fillStyle = 'white';
        ctx.fill();

        ctx.strokeStyle = strokeColor;
        ctx.lineWidth = 0.5;
        ctx.stroke();

        ctx.restore();
    }

    function drawRoutes() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        route_path.forEach(route => {
            if (route.length < 2) return;

            // --- Outer stroke (outline) ---
            ctx.beginPath();
            ctx.moveTo(route[0].x, route[0].y);
            for (let i = 1; i < route.length; i++) {
                ctx.lineTo(route[i].x, route[i].y);
            }
            ctx.strokeStyle = 'rgba(0, 0, 0, 0.8)';
            ctx.lineWidth = 10;
            ctx.lineJoin = 'round';
            ctx.lineCap = 'round';
            ctx.stroke();

            // --- Inner stroke (main visible line) ---
            ctx.beginPath();
            ctx.moveTo(route[0].x, route[0].y);
            for (let i = 1; i < route.length; i++) {
                ctx.lineTo(route[i].x, route[i].y);
            }
            ctx.strokeStyle = 'rgba(255, 0, 0, 0.85)';
            ctx.lineWidth = 6;
            ctx.lineJoin = 'round';
            ctx.lineCap = 'round';
            ctx.stroke();
        });

        // --- Draw pins ---
        route_path.forEach(route => {
            for (let i = 0; i < route.length; i++) {
                drawPin(route[i].x, route[i].y);
            }
        });
    }

    // If the image has already loaded before the onload is assigned (from cache)
    if (image.complete) {
        image.onload();
    }
});