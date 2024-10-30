import sys
from bs4 import BeautifulSoup


def modify_html(file_path, output_name):
    # Charger le fichier HTML
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")

    # 1. Remplacer "NAMEFILE_files" par "quarto_files"
    head = soup.find("head")
    for link_tag in head.find_all("link"):
        link_tag["href"] = "quarto_files/" + "/".join(link_tag["href"].split("/")[1:])
    for script_tag in head.find_all("script"):
        script_tag["src"] = "quarto_files/" + "/".join(script_tag["src"].split("/")[1:])
        script_tag["type"] = "module"

    # 2. Modifier la balise body
    body = soup.body
    body["class"] = (
        "bg-slate-100 fullContent w-screen overflow-x-hidden bg-gray-100 font-body text-gray-900"
    )

    # 3. Supprimer la feuille de style Bootstrap
    bootstrap_link = soup.find("link", {"id": "quarto-bootstrap"})
    if bootstrap_link:
        bootstrap_link.decompose()

    # 4. Ajouter Tailwind CSS dans le head
    head = soup.head
    tailwind_link = soup.new_tag("link", rel="stylesheet", href="../build/tailwind.css")
    head.append(tailwind_link)
    font_link = soup.new_tag(
        "link", rel="preconnect", href="https://fonts.googleapis.com"
    )
    head.append(font_link)
    font_link2 = soup.new_tag(
        "link",
        rel="preconnect",
        href="https://fonts.gstatic.com",
        attrs={"crossorigin": ""},
    )
    head.append(font_link2)
    font_link3 = soup.new_tag(
        "link",
        rel="stylesheet",
        href="https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100..700;1,100..700&display=swap",
    )
    head.append(font_link3)

    # 5. Modifier les classes de #quarto-content
    quarto_content = soup.find(id="quarto-content")
    if quarto_content:
        quarto_content["class"] = (
            "px-6 pb-16 pt-48 lg:pt-16 sm:px-16 sm:pl-52 lg:pl-72 xl:pl-96"
        )

    # 6. Modifier les classes des titres
    for h1 in soup.find_all("h1"):
        h1["class"] = (
            "font-heading text-4xl !w-full max-w-[40rem] sm:text-6xl mb-12 mt-8 font-normal text-center"
        )
    title_header = soup.find(id="title-block-header")
    title_header["class"] = "prose lg:prose-lg text-center font-normal"
    for h2 in soup.find_all("h2"):
        h2["class"] = (
            "text-2xl sm:text-3xl !w-full max-w-[40rem] mb-4 mt-8 font-bold text-pacific-blue-600"
        )
    for h3 in soup.find_all("h3"):
        h3["class"] = (
            "text-lg sm:text-2xl !w-full max-w-[40rem] mb-4 mt-8 font-bold text-pacific-blue-900"
        )
    for h4 in soup.find_all("h4"):
        h4["class"] = (
            "text-base sm:text-xl !w-full max-w-[40rem] mb-4 mt-8 font-bold text-pacific-blue-900"
        )

    # 7. Ajouter des classes à sourceCode, s'il n'est pas dans un div avec la classe "cell"
    for source_code in soup.find_all(class_="sourceCode"):
        if (
            source_code.parent.name == "div"
            and not source_code.find_parent(class_="cell")
            and not source_code.find_parent(class_="code-with-filename")
        ):
            source_code["class"] = (
                " ".join(source_code["class"])
                + " overflow-auto !max-w-[40rem] text-sm lg:text-base mb-8 p-2 shadow-gray-900 shadow-punk border border-gray-900"
            ).split(" ")
        if (
            source_code.parent.name == "div"
            and not source_code.find_parent(class_="sourceCode")
            and not source_code.find_parent(class_="code-with-filename")
        ):
            source_code["class"] = (" ".join(source_code["class"]) + " mt-4").split(" ")
        if (
            source_code.parent.name == "div"
            and not source_code.find_parent(class_="sourceCode")
            and source_code.find_parent(class_="code-with-filename")
        ):
            source_code["class"] = (
                " ".join(source_code["class"])
                + " !mt-0  overflow-auto !max-w-[40rem] text-sm lg:text-base mb-8 p-2 shadow-gray-900 shadow-punk border border-gray-900"
            ).split(" ")
        if source_code.parent.name == "section":
            source_code["class"] = ("mb-4").split(" ")
    for filename in soup.find_all(class_="code-with-filename-file"):
        filename["class"] = (
            " ".join(filename["class"])
            + " bg-gray-900 inline-block text-gray-100 py-1 px-2 -rotate-3"
        )
    for filename in soup.find_all(class_="code-with-filename"):
        filename["class"] = " ".join(filename["class"]) + " mt-4"

    # 8. Ajouter des classes aux éléments avec la classe "cell"
    for cell in soup.find_all(class_="cell"):
        cell["class"] = (
            " ".join(cell["class"])
            + " overflow-auto  !max-w-[40rem] text-sm lg:text-base mb-8 mt-4 p-2 shadow-gray-900 shadow-punk border border-gray-900"
        )

    # 9. Ajouter des classes aux éléments avec la classe "cell-output"
    for cell_output in soup.find_all(class_="cell-output"):
        cell_output["class"] = (
            " ".join(cell_output["class"]) + " bg-gray-200 p-2 shadow-inner"
        )

    # 10. Modifier les classes des balises <img>
    for img in soup.find_all("img"):
        img["class"] = (
            "shadow-punk border border-gray-900 p-2 shadow-gray-900 !mt-8 !mb-10"
        )
        # Compress images
        img["src"] = img["src"] + "?as=webp&quality=80&width=800"

    # 11. Ajouter le script pour les iframes à la fin
    body = soup.body
    demo_script = soup.new_tag("script", src="../js/iframe_demo.js")
    head.append(demo_script)
    menu_script = soup.new_tag("script", src="../js/ts/menu.ts")
    head.append(menu_script)

    # 12. Ajouter un menu au début du body
    nav_html = """
		<nav class="fixed isolate w-52 z-50 m-0 p-4 text-xl lg:m-8">
			<a
				class="w-full border-b inline-block border-pink-800 bg-gray-200 px-1 pb-1 pt-2 not-italic lg:bg-transparent"
				href=""
				>Thomas Dargent</a
			>
			<button id="show-btn" class="-rotate-1 rotate-1 shadow-md sm:hidden w-full bg-gray-100  border border-pink-950 text-center" type="button">↧</button>
			<ul id="menu" class="mt-4 *:bg-gray-200 *:lg:bg-transparent hidden sm:block text-base">
				<li class="p-1 hover:ml-4 hover:text-pacific-blue-600">
					<a href="#portfolio">Portfolio</a>
				</li>
				<li class="p-1 hover:ml-4 hover:text-pacific-blue-600"><a href="#blog">Blog</a></li>
				<li class="px-1 hover:ml-4 hover:text-pacific-blue-600"><a href="#contact">Contact</a></li>
			</ul>
		</nav>
    """
    nav_tag = BeautifulSoup(nav_html, "lxml").nav
    body.insert(0, nav_tag)

    # 13. Mettre --tw-prose-pre-code et --tw-prose-pre-bg à 'null' pour tous les éléments <pre>
    for pre in soup.find_all("pre"):
        style_attr = pre.get("style", "")
        # Ajouter les nouveaux styles tout en conservant les styles existants
        new_style = " --tw-prose-pre-code: null; --tw-prose-pre-bg: null;"
        pre["style"] = style_attr + new_style

    # 14. Mettre en forme le texte
    main = soup.find("main")
    if main:
        for p in main.find_all("p"):  # Ne trouve que les <p> directement dans <main>
            p["class"] = (
                "prose lg:prose-lg !w-full max-w-[40em] prose-stone max-w-[40em]  mb-4"
            )
            for code in p.find_all("code"):
                code["class"] = "p-1 text-pink-600 shadow-inner"
        for ul in main.find_all("ul"):
            ul["class"] = (
                "prose prose-stone !w-full max-w-[40em]  list-disc pl-8 lg:prose-lg"
            )
            print(ul)
            for code in ul.find_all("code"):
                code["class"] = "p-1 text-pink-600 shadow-inner"
        for ol in main.find_all("ol"):
            ol["class"] = (
                "prose prose-stone !w-full max-w-[40em] list-decimal pl-8 lg:prose-lg"
            )
            for code in ol.find_all("code"):
                code["class"] = "p-1 text-pink-600 shadow-inner"
        for table in main.find_all(
            "table", recursive=False
        ):  # Ne trouve que les table directement dans <main>
            table.parent["class"] = "prose-sm lg:prose-base prose-stone"
            for code in table.find_all("code"):
                code["class"] = "p-1 text-pink-600 shadow-inner"
    sections = soup.find_all("section")
    if sections:
        for section in sections:
            for p in section.find_all(
                "p", recursive=False
            ):  # Ne trouve que les <p> directement dans une section
                p["class"] = "prose lg:prose-lg !w-full prose-stone max-w-[40rem] mb-4"
    # 15. Subtitle
    for p in soup.find_all(
        "p", string=lambda text: text and text.startswith("|") and text.endswith("|")
    ):
        p["class"] = (
            "prose lg:prose-lg text-lg !mb-16 !w-full max-w-[40rem] text-gray-900 text-center".split(
                " "
            )
        )
        p["role"] = "doc-subtitle"
        p.string = "“" + p.text.strip("|").strip() + "”"

        or_tag = soup.new_tag("p")
        or_tag["class"] = (
            "prose lg:prose-lg text-xl !w-full max-w-[40rem] text-gray-700 !mb-6 !mt-2 text-gray-900 text-center".split(
                " "
            )
        )
        or_tag.string = "— OR —"
        title_header.append(or_tag)
        title_header.append(p)

    # Sauvegarder le fichier modifié
    with open(
        "/".join(file_path.split("/")[:-1]) + "/" + output_name, "w", encoding="utf-8"
    ) as file:
        file.write(str(soup))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python modify_html.py <file_path> <output_name>")
        sys.exit(1)

    html_file = sys.argv[1]
    output_name = sys.argv[2]
    modify_html(html_file, output_name)
    print(f"Modifications apportées à {html_file}")
