function generatePapyrusTexture() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const width = window.innerWidth;
    const height = window.innerHeight;

    canvas.width = width;
    canvas.height = height;

    // --- Base color of background ---
    ctx.fillStyle = '#fdf6e3';
    ctx.fillRect(0, 0, width, height);

    // --- Vertical fibers ---
    for (let i = 0; i < width * 4; i++) {
        const x = Math.random() * width;
        const y = Math.random() * height;
        const w = Math.random() * 1 + 0.3;
        const h = Math.random() * 30 + 10;
        const alpha = Math.random() * 0.05 + 0.01;
        ctx.fillStyle = `rgba(200, 170, 120, ${alpha})`;
        ctx.fillRect(x, y, w, h);
    }

    // --- Horizontal fibers ---
    for (let i = 0; i < height * 3; i++) {
        const x = Math.random() * width;
        const y = Math.random() * height;
        const w = Math.random() * 30 + 10;
        const h = Math.random() * 1 + 0.3;
        const alpha = Math.random() * 0.04 + 0.01;
        ctx.fillStyle = `rgba(180, 140, 100, ${alpha})`;
        ctx.fillRect(x, y, w, h);
    }

    // --- Darker edges ---
    const gradient = ctx.createRadialGradient(
        width / 2,
        height / 2,
        width / 4,
        width / 2,
        height / 2,
        Math.max(width, height)
    );
    gradient.addColorStop(0, 'rgba(255, 255, 240, 0)');
    gradient.addColorStop(1, 'rgba(100, 80, 50, 0.3)');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, width, height);

    //  --- Stains and discolorations ---
    for (let i = 0; i < 6; i++) {
        const cx = Math.random() * width;
        const cy = Math.random() * height;
        const maxRadius = 60 + Math.random() * 40;
        const ringWidth = 6 + Math.random() * 4;

        for (let j = 0; j < 10; j++) {
            const radius = maxRadius - j * (ringWidth / 2);
            const alpha = 0.02 + Math.random() * 0.03;

            ctx.beginPath();
            ctx.arc(
                cx + Math.random() * 10 - 5,
                cy + Math.random() * 10 - 5,
                radius,
                0,
                2 * Math.PI
            );
            ctx.strokeStyle = `rgba(120, 90, 50, ${alpha})`;
            ctx.lineWidth = 1 + Math.random() * 1.5;
            ctx.stroke();
        }
    }

    // --- Set as background ---
    const dataURL = canvas.toDataURL('image/png');
    document.body.style.backgroundImage = `url(${dataURL})`;
}

window.addEventListener('DOMContentLoaded', generatePapyrusTexture);