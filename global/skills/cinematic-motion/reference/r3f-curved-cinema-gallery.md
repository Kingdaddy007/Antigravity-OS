# WebGL Curved Cinema Gallery (R3F)

Use this when a portfolio or material archive should feel like a rotating private gallery, panoramic room wall, or immersive showroom object. 

## When To Use
- Signature portfolio reel where rooms wrap around the visitor.
- Gallery-like residential curation where images become an environment.
- When you need a frictionless, drag-to-explore 3D space.

## Core R3F Architecture
Instead of drawing all images to one massive texture (which hits GPU limits), render each image as its own distinct `<GalleryPanel>` mapped to a slice of a `<cylinderGeometry>`.

## The Two Golden Fixes for 3D Galleries

### 1. Dynamic FOV Scaling (The Size Problem)
**Problem:** In a closed 360-degree cylinder, 11 panels must be thinner than 4 panels. If you want all galleries to look the same size regardless of image count, you cannot use a fixed camera FOV.
**Solution:** Dynamically zoom the camera (adjust FOV) based on the image count `N`. Establish a "perfect" baseline (e.g., 6 images look perfect at 35° FOV), and scale the rest.

```javascript
// Formula to normalize perceived panel size across any array length:
const N = images.length;
const baseN = 6;
const baseFov = 35; 
const baseTan = Math.tan((baseFov / 2) * (Math.PI / 180));
const targetTan = (baseN / N) * baseTan;
const dynamicFov = 2 * Math.atan(targetTan) * (180 / Math.PI);

// Apply to <Canvas camera={{ fov: dynamicFov }}>
```

### 2. Dynamic Polar Limits (The Trackpad Drift Problem)
**Problem:** Trackpad users rarely swipe perfectly horizontally. The resulting diagonal drift causes the camera to "nod" up and down. When heavily zoomed in (small FOV), a tiny nod throws the images completely off the screen, ruining the UX.
**Solution:** Do not use fixed polar angles. Restrict the vertical look allowance to a percentage of the current FOV (e.g., 8%). This allows a premium, subtle "nod" without letting the user get lost.

```javascript
// Limit vertical look to 8% of the dynamic FOV
const polarLimit = (dynamicFov * (Math.PI / 180)) * 0.08;

// Apply to <OrbitControls 
//   minPolarAngle={Math.PI / 2 - polarLimit} 
//   maxPolarAngle={Math.PI / 2 + polarLimit} 
// />
```

## Cinematic Atmosphere Setup
A pure black void destroys depth perception. Always include:
1. **Reflective Horizon:** Ground the cylinder by placing a dark `<MeshReflectorMaterial>` plane directly beneath it. This gives a physical floor and horizon line.
2. **Volumetric Dust:** Suspend `<Sparkles>` inside the cylinder. When the user drags to rotate, these particles move, providing instant, massive parallax depth cues.
3. **Scaled Fog:** Use `<fog attach="fog" args={['#hex', radius * 0.8, radius * 1.5]} />`. Ensure the fog start/end scales with the calculated `radius` of the room, otherwise large rooms (high N) will be swallowed by darkness.
