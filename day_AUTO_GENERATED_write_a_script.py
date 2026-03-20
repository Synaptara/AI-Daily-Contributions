import math

def calculate_circle_properties(radius):
    # calculate area of circle using formula: pi * r^2
    area = math.pi * (radius ** 2)
    
    # calculate circumference of circle using formula: 2 * pi * r
    circumference = 2 * math.pi * radius
    
    return area, circumference

def main():
    radius = float(input("Enter the radius of the circle: "))
    
    area, circumference = calculate_circle_properties(radius)
    
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")

if __name__ == "__main__":
    main()