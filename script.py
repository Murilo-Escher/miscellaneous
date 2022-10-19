import fitz

doc = fitz.open("folien.pdf")

size = doc.page_count

output_pdf = "output.pdf"

list_of_pages = []

for i in range(2, size):
    previousPage = doc[i - 1]
    page = doc[i]

    wordsPreviousPage = previousPage.get_textpage().extractWORDS()
    for word in wordsPreviousPage:
        if word[4].isnumeric():
            break
    previousPageNumber = word[4]

    wordsPage = page.get_textpage().extractWORDS()
    for word in wordsPage:
        if word[4].isnumeric():
            break
    currentPageNumber = word[4]

    if currentPageNumber == previousPageNumber:
        list_of_pages.append(i - 1)

doc.delete_pages(list_of_pages)

doc.save(output_pdf)

doc.close()
