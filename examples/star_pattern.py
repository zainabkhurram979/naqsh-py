import nakshpy as nk

# Generate an 8-point star
star = nk.star_pattern(points=8, outer_radius=2, inner_radius=1)

# Rotate it
star = nk.rotate(star, 30)

# Draw it
nk.draw(star)

# Save it
nk.save("star_pattern.png")
