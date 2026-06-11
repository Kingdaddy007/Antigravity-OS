# Synchronized Dynamic Scroll List Pinning

## Visual Description
The left half of the screen contains a long list of character or product names. The right half contains a single large image area. As the user scrolls down the list, the entire section pins to the screen. The list continues to scroll natively, but precisely as a new name hits the center "active" zone of the list, the image on the right smoothly transitions to match the active name. The transition is governed strictly by the scroll progress, meaning the user can hold the scroll halfway between two names and see a half-faded hybrid of the two images.

## Emotional Register
Editorial, crisp, and deeply connected. The interface feels completely subordinate to the user's thumb velocity.

## Technical Mechanics
- **DOM Structure:** Flex or grid layout. `.left-list` wrapping `<ul><li>`, `.right-preview` wrapping stacked absolute `<img>` tags.
- **JS Engine:** GSAP ScrollTrigger, Lenis Smooth Scroll.
- **Key Timeline Logic:** Dynamic scroll calculation. `ScrollTrigger.create()` utilizing `pin: true` on the parent wrapper. `onUpdate` callbacks track the exact pixel distance scrolled to calculate which `<li>` element currently intersects the center threshold.
- **Easing Curve:** `scrub: true` translates to direct 1:1 playback based on Lenis inertia.

## Code Snippet / Reverse Engineering Brief
```javascript
import gsap from "gsap";
import ScrollTrigger from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const listItems = document.querySelectorAll(".left-list li");
const totalItems = listItems.length;

ScrollTrigger.create({  
  trigger: ".roster-section",  
  pin: true,  
  start: "top top",  
  end: () => `+=${document.querySelector(".left-list").offsetHeight}`,  
  onUpdate: (self) => {  
    // Math to determine which list item is active based on self.progress  
    // Limit activeIndex to totalItems - 1 to prevent out-of-bounds
    const activeIndex = Math.min(Math.floor(self.progress * totalItems), totalItems - 1);  
      
    // Switch images cleanly without jumping  
    gsap.to(".preview-img", {  
      opacity: (i) => i === activeIndex ? 1 : 0,  
      duration: 0.3, // Allows slight overlap  
      overwrite: "auto"  
    });  
  }  
});
```

## Metadata
- **Industry Name(s):** Pinned Roster Gallery, Scrubbed Index Preview
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH
- **Accessibility / Reduced Motion:** Transition to simple scrolling without pinning if `prefers-reduced-motion` is enabled, or shorten transitions.
