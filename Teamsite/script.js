particlesJS("particle-js", {
    particles: {
        number: {
            value: 80, // Number of particles
            density: {
                enable: true,
                value_area: 800
            }
        },
        // ... Other particle properties ...

        move: {
            enable: true,
            speed: 6, // Speed of particles' movement
            direction: "none",
            random: false,
            straight: false,
            out_mode: "out",
            bounce: false,
            attract: {
                enable: false,
                rotateX: 600,
                rotateY: 1200
            }
        }
    },
    interactivity: {
        detect_on: "canvas",
        events: {
            onhover: {
                enable: true,
                mode: "repulse" // Use "repulse" mode on hover
            },
            onclick: {
                enable: true,
                mode: "push" // Interaction mode on click (push, remove, bubble, etc.)
            },
            resize: true
        },
        modes: {
            repulse: {
                distance: 100, // Adjust this distance to control the repulsion strength
                duration: 0.4
            },
            // ... Other interaction modes ...
        }
    },
    retina_detect: true
});