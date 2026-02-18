import re
import requests
import os

# Paste your HTML block between triple quotes
html = """
<div class="file_list" id="file_list_2025"><a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1535.PDF" target="_blank">PD1535</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1536.PDF" target="_blank">PD1536</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1537.PDF" target="_blank">PD1537</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1540.PDF" target="_blank">PD1540</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1610.PDF" target="_blank">PD1610</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1615.PDF" target="_blank">PD1615</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1620.PDF" target="_blank">PD1620</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1625.PDF" target="_blank">PD1625</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1630.PDF" target="_blank">PD1630</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1631.PDF" target="_blank">PD1631</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1632.PDF" target="_blank">PD1632</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1633.PDF" target="_blank">PD1633</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1634.PDF" target="_blank">PD1634</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1635.PDF" target="_blank">PD1635</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1636.PDF" target="_blank">PD1636</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1640.PDF" target="_blank">PD1640</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1645.PDF" target="_blank">PD1645</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1670.PDF" target="_blank">PD1670</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1675.PDF" target="_blank">PD1675</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1680.PDF" target="_blank">PD1680</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1685.PDF" target="_blank">PD1685</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1690.PDF" target="_blank">PD1690</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1695.PDF" target="_blank">PD1695</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1700.PDF" target="_blank">PD1700</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1701.PDF" target="_blank">PD1701</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1705.PDF" target="_blank">PD1705</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1706.PDF" target="_blank">PD1706</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1707.PDF" target="_blank">PD1707</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1708.PDF" target="_blank">PD1708</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1710.PDF" target="_blank">PD1710</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1715.PDF" target="_blank">PD1715</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1750.PDF" target="_blank">PD1750</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1755.PDF" target="_blank">PD1755</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1760.PDF" target="_blank">PD1760</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1875.PDF" target="_blank">PD1875</a> <a href="https://ebctt.com/wp-content/uploads/annual_list/2025/TUNAPUNA/PD1880.PDF" target="_blank">PD1880</a> </div>
"""
# Extract all PDF URLs
urls = re.findall(r'https://[^"]+\.PDF', html)
name = "TUNAPUNA"
# Create folder
os.makedirs(f"Locations pdfs/{name}", exist_ok=True)

for url in urls:
    filename = url.split("/")[-1]
    print("Downloading:", filename)

    r = requests.get(url)

    if r.status_code == 200:
        with open(f"Locations pdfs/{name}/{filename}", "wb") as f:
            f.write(r.content)

print("Done.")
