import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Lenis from "lenis";

document.addEventListener("DOMContentLoaded", () => {
  gsap.registerPlugin(ScrollTrigger);

  const lenis = new Lenis();
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });
  gsap.ticker.lagSmoothing(0);

  const smoothStep = (p) => p * p * (3 - 2 * p);

  if (window.innerWidth > 1000) {
    // 👉 카드 id 배열을 변수로 분리 (추가함)
    const heroCardIds = ["#hero-card-1", "#hero-card-2", "#hero-card-3", "#hero-card-4", "#hero-card-5"];
    const servicesCardIds = ["#card-1", "#card-2", "#card-3", "#card-4", "#card-5"];

    // 👉 하드코딩 값과 동일하게 나오도록 자동 계산 수정
    const cardCount = heroCardIds.length;
    
    // Hero 섹션 - 하드코딩 값: ["150%", "85%", "0%", "-85%", "-150%"]
    const spreadX = heroCardIds.map((_, i) => {
      if (i === 0) return "150%";
      if (i === 1) return "85%";
      if (i === 2) return "0%";
      if (i === 3) return "-85%";
      if (i === 4) return "-150%";
      // 추가 카드가 있을 경우를 위한 일반 공식
      const centerIndex = Math.floor(cardCount / 2);
      if (i < centerIndex) {
        return `${150 - (centerIndex - i - 1) * 65}%`;
      } else if (i > centerIndex) {
        return `${-150 + (centerIndex - i + 1) * 65}%`;
      }
      return "0%";
    });

    // Hero 섹션 - 하드코딩 값: [-15, -7.5, 0, 7.5, 15]
    const spreadRotate = heroCardIds.map((_, i) => {
      if (i === 0) return -15;
      if (i === 1) return -7.5;
      if (i === 2) return 0;
      if (i === 3) return 7.5;
      if (i === 4) return 15;
      // 추가 카드가 있을 경우를 위한 일반 공식
      const centerIndex = Math.floor(cardCount / 2);
      return (i - centerIndex) * 7.5;
    });

    ScrollTrigger.create({
      trigger: ".hero",
      start: "top top",
      end: "75% top",
      scrub: 1,
      onUpdate: (self) => {
        const progress = self.progress;

        const heroCardsContainerOpacity = gsap.utils.interpolate(
          1,
          0.5,
          smoothStep(progress)
        );
        gsap.set(".hero-cards", {
          opacity: heroCardsContainerOpacity,
        });

        heroCardIds.forEach((cardId, index) => {
          const delay = index * 0.9;
          const cardProgress = gsap.utils.clamp(
            0,
            1,
            (progress - delay * 0.1) / (1 - delay * 0.1)
          );

          const y = gsap.utils.interpolate(
            "0%",
            "350%",
            smoothStep(cardProgress)
          );
          const scale = gsap.utils.interpolate(
            1,
            0.75,
            smoothStep(cardProgress)
          );

          const x = gsap.utils.interpolate("0%", spreadX[index], smoothStep(cardProgress));
          const rotation = gsap.utils.interpolate(0, spreadRotate[index], smoothStep(cardProgress));

          gsap.set(cardId, {
            y: y,
            x: x,
            rotation: rotation,
            scale: scale,
          });
        });
      },
    });

    ScrollTrigger.create({
      trigger: ".services",
      start: "top top",
      end: `+=${window.innerHeight * 4}px`,
      pin: ".services",
      pinSpacing: true,
    });

    ScrollTrigger.create({
      trigger: ".services",
      start: "top top",
      end: `+=${window.innerHeight * 4}px`,
      onLeave: () => {
        const servicesSection = document.querySelector(".services");
        const servicesRect = servicesSection.getBoundingClientRect();
        const servicesTop = window.pageYOffset + servicesRect.top;

        gsap.set(".cards", {
          position: "absolute",
          top: servicesTop,
          left: 0,
          width: "100vw",
          height: "100vh",
        });
      },
      onEnterBack: () => {
        gsap.set(".cards", {
          position: "fixed",
          top: 0,
          left: 0,
          width: "100vw",
          height: "100vh",
        });
      },
    });

    ScrollTrigger.create({
      trigger: ".services",
      start: "top bottom",
      end: `+=${window.innerHeight * 4}`,
      scrub: 1,
      onUpdate: (self) => {
        const progress = self.progress;

        const headerProgress = gsap.utils.clamp(0, 1, progress / 0.9);
        const headerY = gsap.utils.interpolate(
          "400%",
          "0%",
          smoothStep(headerProgress)
        );
        gsap.set(".services-header", {
          y: headerY,
        });

        servicesCardIds.forEach((cardId, index) => {
          const delay = index * 0.5;
          const cardProgress = gsap.utils.clamp(
            0,
            1,
            (progress - delay * 0.1) / (0.9 - delay * 0.1)
          );

          const innerCard = document.querySelector(`${cardId} .flip-card-inner`);

          let y;
          if (cardProgress < 0.4) {
            const normalizedProgress = cardProgress / 0.4;
            y = gsap.utils.interpolate("-100%", "50%", smoothStep(normalizedProgress));
          } else if (cardProgress < 0.6) {
            const normalizedProgress = (cardProgress - 0.4) / 0.2;
            y = gsap.utils.interpolate("50%", "0%", smoothStep(normalizedProgress));
          } else {
            y = "0%";
          }

          let scale;
          if (cardProgress < 0.4) {
            const normalizedProgress = cardProgress / 0.4;
            scale = gsap.utils.interpolate(0.25, 0.75, smoothStep(normalizedProgress));
          } else if (cardProgress < 0.6) {
            const normalizedProgress = (cardProgress - 0.4) / 0.2;
            scale = gsap.utils.interpolate(0.75, 1, smoothStep(normalizedProgress));
          } else {
            scale = 1;
          }

          let opacity;
          if (cardProgress < 0.2) {
            const normalizedProgress = cardProgress / 0.2;
            opacity = smoothStep(normalizedProgress);
          } else {
            opacity = 1;
          }

          // Services 섹션도 자동 계산으로 변경 (하드코딩 값과 동일하게)
          // 하드코딩 값: ["200%", "100%", "0%", "-100%", "-200%"]
          const servicesSpreadX = servicesCardIds.map((_, i) => {
            if (i === 0) return "200%";
            if (i === 1) return "100%";
            if (i === 2) return "0%";
            if (i === 3) return "-100%";
            if (i === 4) return "-200%";
            // 추가 카드가 있을 경우를 위한 일반 공식
            const centerIndex = Math.floor(servicesCardIds.length / 2);
            return `${(i - centerIndex) * 100}%`;
          });

          // 하드코딩 값: [-8, -4, 0, 4, 8]
          const servicesSpreadRotate = servicesCardIds.map((_, i) => {
            if (i === 0) return -8;
            if (i === 1) return -4;
            if (i === 2) return 0;
            if (i === 3) return 4;
            if (i === 4) return 8;
            // 추가 카드가 있을 경우를 위한 일반 공식
            const centerIndex = Math.floor(servicesCardIds.length / 2);
            return (i - centerIndex) * 4;
          });

          let x, rotate, rotationY;
          if (cardProgress < 0.6) {
            x = servicesSpreadX[index];
            rotate = servicesSpreadRotate[index];
            rotationY = 0;
          } else if (cardProgress < 1) {
            const normalized = smoothStep((cardProgress - 0.6) / 0.4);
            x = gsap.utils.interpolate(servicesSpreadX[index], "0%", normalized);
            rotate = gsap.utils.interpolate(servicesSpreadRotate[index], 0, normalized);
            rotationY = normalized * 180;
          } else {
            x = "0%";
            rotate = 0;
            rotationY = 180;
          }

          gsap.set(cardId, {
            opacity: opacity,
            y: y,
            x: x,
            rotate: rotate,
            scale: scale,
          });

          gsap.set(innerCard, {
            rotationY: rotationY,
          });
        });
      },
    });
  }
});