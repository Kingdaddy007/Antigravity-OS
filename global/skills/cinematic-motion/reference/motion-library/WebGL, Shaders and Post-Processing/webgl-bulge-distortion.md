# WebGL Bulge Distortion

## Visual Description
A magnifying bulge effect follows the cursor over imagery, resembling a glass sphere rolling over a flat plane.

## Emotional Register
Playful and curious.

## Technical Mechanics
- **JS Engine:** OGL Library.
- **Shader/WebGL:** Vertex distortion pushing geometry toward the camera along the Z-axis based on cursor distance.

## Code Snippet / Reverse Engineering Brief
**Reverse Engineering Brief:** Pass the cursor position as a uniform (`u_mouse`). In the vertex shader, calculate the distance between the current vertex and the `u_mouse` coordinates. Apply a radial falloff function (like `smoothstep`) to this distance. Displace the vertex along the positive Z-axis based on the inverse of this distance, creating a localized 3D bulge that perfectly aligns with the cursor's movement.

## Metadata
- **Industry Name(s):** Magnifying Lens Distortion
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH
- **Accessibility / Reduced Motion:** Disable the bulge distortion or replace it with a standard opacity hover effect if reduced motion is requested.
