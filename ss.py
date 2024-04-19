import pyautogui

def take_screenshot():
    x = 0  # X-coordinate of the top-left corner of the region
    y = 120  # Y-coordinate of the top-left corner of the region
    width = 1920  # Width of the region
    height = 950  # Height of the region
    save_path = "map.png"  # Path where the screenshot will be saved
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(save_path)

# Example usage:


take_screenshot()
