# Refraction / Glass Distortion

## Visual Description
Background content is distorted through a "glass" or refractive surface (often an image, logo, or shape overlay). The distortion mimics light refraction through curved glass or water — background pixels appear bent/shifted based on surface normals. Often implemented with a normal map (texture encoding surface orientation) that offsets background UV sampling. Creates depth and material realism — the "glass" element feels tangible and volumetric. The effect is static or animated (e.g., liquid surface rippling, glass rotating).

## Emotional Register
Sophisticated, material, dimensional, tactile. Adds realism and depth. Conveys luxury and craftsmanship (glass, water, crystal materials). Appropriate for luxury goods, cosmetics, beverages, architectural visualization.

## Technical Mechanics
- **DOM Structure:** WebGL scene with background texture and foreground "glass" plane with normal map
- **CSS Properties:** N/A
- **JS Engine:** Three.js with custom shader
- **Key Timeline Logic:** Fragment shader samples normal map, calculates refraction vector, offsets background UV lookup
- **Easing Curve:** N/A (shader effect is instantaneous)
- **Performance Notes:** Sampling two textures per pixel (normal + background) is moderately expensive but acceptable. Ensure normal map is compressed (JPEG at low quality sufficient).

## Code Snippet / Reverse Engineering Brief
```glsl
uniform sampler2D uBackground;
uniform sampler2D uNormalMap;
varying vec2 vUv;

void main() {
  vec3 normal = texture2D(uNormalMap, vUv).rgb * 2.0 - 1.0; // remap [0,1] to [-1,1]
  vec2 refractedUV = vUv + normal.xy * 0.05; // offset background UV by normal
  vec4 background = texture2D(uBackground, refractedUV);
  gl_FragColor = background;
}
```

**Reverse Engineering Brief:**
Production examples use proprietary shaders with complex normal/environment mapping. To recreate basic refraction:
1. **Setup Scene**: Render background content to render texture, overlay foreground "glass" plane
2. **Normal Map**: Create or source normal map texture (encodes surface bumps/curvature as RGB values)
3. **Refraction Shader**: Sample normal map, convert RGB to normal vector, use to offset background UV coordinates
4. **Tuning**: Adjust refraction strength (multiplier on normal offset), Fresnel effect (edge vs. center refraction), chromatic aberration (separate RGB offsets for realistic dispersion)

Advanced: Add Fresnel term (edges refract more than center), environment mapping (reflections), and chromatic aberration (RGB channels refract at different angles).

## Metadata
- **Industry Name(s):** Refraction Effect, Glass Shader, Distortion Map
- **Rarity:** RARE
- **Implementation Confidence:** MEDIUM
- **Production Feasibility:** MEDIUM — Requires 3-4 day dev investment, WebGL/shader expertise, and high-quality normal maps (design asset). Limited mobile support (performance).
- **Accessibility / Reduced Motion:** Refraction is static (no animation); no `prefers-reduced-motion` adaptation required. Ensure text overlaid on refracted backgrounds remains legible (test contrast, avoid text directly behind high-distortion areas).
