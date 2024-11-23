import sys
from bs4 import BeautifulSoup
from pathlib import Path

def modify_html(folder_path: Path, filename, output_name):
    processed = []
    print(f"Processing files in {folder_path.absolute()}")
    for file_path in folder_path.iterdir():
        if file_path.is_dir() or file_path.suffix != ".html":
            continue
        if filename is not None and file_path != filename:
            continue
        print("\033[1;34m#", end="")

        # Charger le fichier HTML
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "lxml")

        # 0. Add HTML attributes
        html = soup.find("html")
        html.attrs = {"lang": "en"}

        # 1. Remplacer "NAMEFILE_files" par "quarto_files"
        head = soup.find("head")
        for link_tag in head.find_all("link"):
            link_tag["href"] = "./quarto_files/" + "/".join(link_tag["href"].split("/")[1:])
        for script_tag in head.find_all("script"):
            if 'src' in script_tag.attrs:
                script_tag["src"] = "./quarto_files/" + "/".join(script_tag["src"].split("/")[1:])
            script_tag["type"] = "module"

        # 2. Modifier la balise body
        body = soup.body
        body["class"] = (
            "bg-gray-100 fullContent w-screen overflow-x-hidden bg-gray-100 font-body text-gray-900 dark:bg-gray-1000 dark:text-gray-200"
        )

        # 3. Supprimer Bootstrap
        bootstrap_links = soup.find_all("link", {"id": "quarto-bootstrap"})
        for bootstrap_link in bootstrap_links:
            bootstrap_link.decompose()
        bootstrap_link = soup.find("link", {"href": "./quarto_files/libs/bootstrap/bootstrap-icons.css"})
        bootstrap_link.decompose()
        bootstrap_script = soup.find("script", {"src": "./quarto_files/libs/bootstrap/bootstrap.min.js"})
        bootstrap_script.decompose()

        # 4. HEAD
        head = soup.head

        favicon = soup.new_tag(
            "link", rel="icon", href="../img/favicon.ico", attrs={"type": "image/x-icon"}
        )
        head.append(favicon)
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
        font_link4 = soup.new_tag(
            "link",
            attrs={
                'rel':"preload",
                'href':"../fonts/LeMurmure-Regular.woff2",
                'as':"font",
                'type':"font/woff2",
                'crossorigin':"anonymous"
            }
        )
        head.append(font_link4)
        tailwind_link = soup.new_tag("link", rel="stylesheet", href="../build/tailwind.css")
        head.append(tailwind_link)
        dark_select_html = """
            <script>
                if (localStorage.getItem('dark-mode') === 'true' || (!('dark-mode' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                    document.querySelector('html').classList.add('dark');
                } else {
                    document.querySelector('html').classList.remove('dark');
                }
            </script>
        """
        dark_select_tag = BeautifulSoup(dark_select_html, "lxml").script
        head.append(dark_select_tag)


        # 5. Modifier les classes de #quarto-content
        quarto_content = soup.find(id="quarto-content")
        if quarto_content:
            quarto_content["class"] = (
                "px-6 pb-16 pt-48 lg:pt-16 sm:px-16 sm:pl-52 lg:pl-72 xl:pl-96"
            )

        # 6. Modifier les classes des titres
        for h1 in soup.find_all("h1"):
            h1["class"] = (
                "font-heading text-4xl !w-full max-w-[40rem] sm:text-6xl mb-12 mt-8 font-normal text-center dark:text-gray-100"
            )
        title_header = soup.find(id="title-block-header")
        title_header["class"] = "prose lg:prose-lg text-center font-normal"
        for h2 in soup.find_all("h2"):
            h2["class"] = (
                "text-2xl sm:text-3xl !w-full max-w-[40rem] mb-4 mt-8 font-bold text-pacific-blue-600 dark:text-pink-400"
            )
        for h3 in soup.find_all("h3"):
            h3["class"] = (
                "text-lg sm:text-2xl !w-full max-w-[40rem] mb-4 mt-8 font-bold text-pacific-blue-900 dark:text-pink-600"
            )
        for h4 in soup.find_all("h4"):
            h4["class"] = (
                "text-base sm:text-xl !w-full max-w-[40rem] mb-4 mt-8 font-bold text-pacific-blue-900 dark:text-pink-600"
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
                    + " overflow-auto !max-w-[40rem] bg-gray-900 dark:bg-gray-1000 text-sm lg:text-base mb-8 p-2 shadow-gray-1000 dark:shadow-gray-700 shadow-punk border border-gray-900 dark:border-gray-700"
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
                    + " !mt-0  overflow-auto !max-w-[40rem] bg-gray-900 dark:bg-gray-1000 text-sm lg:text-base mb-8 p-2 shadow-gray-1000 dark:shadow-gray-700 shadow-punk border border-gray-900 dark:border-gray-700"
                ).split(" ")
            if source_code.parent.name == "section":
                source_code["class"] = ("mb-4").split(" ")
        for code_filename in soup.find_all(class_="code-with-filename-file"):
            code_filename["class"] = (
                " ".join(code_filename["class"])
                + " bg-gray-900 inline-block text-gray-100 dark:bg-gray-200 dark:text-gray-900 py-1 px-2 -rotate-3"
            )
        for code_filename in soup.find_all(class_="code-with-filename"):
            code_filename["class"] = " ".join(code_filename["class"]) + " mt-4"

        # 8. Ajouter des classes aux éléments avec la classe "cell"
        for cell in soup.find_all(class_="cell"):
            cell["class"] = (
                " ".join(cell["class"])
                + " overflow-auto  !max-w-[40rem] bg-gray-900 dark:bg-gray-1000 text-sm lg:text-base mb-8 mt-4 p-2 shadow-gray-1000 dark:shadow-gray-700 shadow-punk border border-gray-900 dark:border-gray-700"
            )

        # 9. Ajouter des classes aux éléments avec la classe "cell-output"
        for cell_output in soup.find_all(class_="cell-output"):
            cell_output["class"] = (
                " ".join(cell_output["class"]) + " bg-gray-200 dark:bg-gray-900 p-2 shadow-inner"
            )

        # 10. Modifier les classes des balises <img>
        for img in soup.find_all("img"):
            img["class"] = (
                "shadow-punk border border-gray-900 p-2 shadow-gray-900 bg-gray-200 !mt-8 !mb-10 dark:shadow-gray-700 dark:border-gray-700"
            )
            # Compress images
            img["src"] = img["src"] + "?as=webp&quality=80&width=800"

        # 11. Ajouter le script pour les iframes à la fin
        body = soup.body
        demo_script = soup.new_tag("script", src="../js/iframe_demo.js")
        body.append(demo_script)
        menu_script = soup.new_tag("script", src="../js/ts/menu.ts")
        body.append(menu_script)
        switch_theme_script = soup.new_tag("script", src="../js/switch_theme.js")
        body.append(switch_theme_script)

        # 12. Ajouter un menu au début du body
        nav_html = """
        <nav class="fixed isolate w-52 dark:w-56 z-50 m-0 p-4 text-xl lg:m-8">
			<a
				class="w-full border-b inline-block border-pink-800 bg-gray-200 px-1 pb-1 pt-2 not-italic lg:bg-transparent dark:border-0 dark:bg-pink-400 dark:text-gray-1000 dark:font-black"
				href="https://thomasdargent.com"
				>Thomas Dargent</a
			>
			<button id="show-btn" class="-rotate-1 rotate-1 shadow-md sm:hidden w-full bg-gray-100  border border-pink-950 text-center dark:bg-gray-900 dark:border-pink-600" type="button">↧</button>
			<ul id="menu" class="mt-4 *:bg-gray-200 *:lg:bg-transparent dark:*:bg-gray-900 dark:border dark:border-pink-400 dark:[&_li+li]:border-t dark:[&_li+li]:border-pink-400 hidden sm:block text-base">
				<li class="p-1">
					<a href="https://thomasdargent.com/#portfolio" class="hover:ml-4 hover:text-pacific-blue-600 dark:hover:text-pink-400">Portfolio</a>
				</li>
				<li class="p-1"><a href="https://thomasdargent.com/#blog"  class=" hover:ml-4 hover:text-pacific-blue-600 dark:hover:text-pink-400">Blog</a></li>
				<li class="p-1"><a href="https://thomasdargent.com/#contact" class="hover:ml-4 hover:text-pacific-blue-600 dark:hover:text-pink-400">Contact</a></li>
			</ul>
			<div class="flex flex-col justify-center mx-6 mt-2 items-center bg-gray-200 border border-pacific-blue-500 lg:border-0 dark:bg-gray-900 lg:bg-transparent rounded-full dark:border dark:border-pink-600">
					<input type="checkbox" name="light-switch" id="light-switch" class="sr-only" />
					<label class="relative cursor-pointer p-1 grid grid-cols-3" for="light-switch">
						<svg class="dark:fill-gray-700 fill-pacific-blue-500 h-4 w-4 mt-1" viewBox="17.6262 123.819 352.1318 344.5168" xmlns="http://www.w3.org/2000/svg">
							<path  d="M 205.513 205.745 C 268.065 204.767 287.003 164.344 287.789 123.819 C 287.499 164.344 301.297 205.092 369.758 205.178 C 298.116 205.93 287.767 247.714 288.352 288.239 C 288.781 247.714 268.065 203.606 205.513 205.745 Z"/>
							<polygon  points="314.275 232.401 322.389 251.392 341.325 259.057 330.842 241.397"/>
							<polygon style="transform-origin: 244.396px 245.729px;" points="230.871 259.057 238.986 240.065 257.921 232.401 247.439 250.06" transform="matrix(-1, 0, 0, -1, 0, 0.000030517578)"/>
							<polygon  points="314.274 177.389 322.388 158.397 341.324 150.733 330.842 168.392"/>
							<polygon style="transform-origin: 244.396px 164.061px;" points="230.871 150.733 238.986 169.724 257.92 177.389 247.439 159.729" transform="matrix(-1, 0, 0, -1, -0.000030517578, 0)"/>
							<path  d="M 162.82 155.163 C 112.361 251.928 90.773 398.67 321.209 399.04 C 141.603 595.849 -165.971 328.478 162.82 155.163 Z"/>
						  </svg>
						  <div class="border-b border-pink-600 h-1/2 w-full"></div>
						<svg class="dark:fill-[#FDD162] fill-gray-700 ml-2 h-6 w-6" viewBox="176.732 48.923 258.842 257.472" xmlns="http://www.w3.org/2000/svg">
							<path d="M 176.732 177.215 C 275.311 175.683 305.157 112.384 306.395 48.923 C 305.938 112.384 327.683 176.192 435.574 176.327 C 322.67 177.504 306.36 242.935 307.283 306.395 C 307.958 242.935 275.311 173.865 176.732 177.215 Z"/>
							<polygon points="348.135 218.956 360.923 248.696 390.764 260.697 374.245 233.044"/>
							<polygon style="transform-origin: 238.011px 239.826px;" points="216.696 260.697 229.484 230.957 259.325 218.956 242.806 246.609" transform="matrix(-1, 0, 0, -1, 0, 0.000030517578)"/>
							<polygon points="348.134 132.81 360.922 103.07 390.763 91.069 374.244 118.722"/>
							<polygon style="transform-origin: 238.01px 111.94px;" points="216.695 91.069 229.483 120.809 259.324 132.81 242.805 105.157" transform="matrix(-1, 0, 0, -1, 0, 0.000015258789)"/>
						  </svg>
						<span class="sr-only">Switch to light / dark version</span>
					</label>
			</div>
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
                    "prose lg:prose-lg !w-full max-w-[40em] prose-stone dark:prose-invert max-w-[40em]  mb-4"
                )
                for code in p.find_all("code"):
                    code["class"] = "p-1 text-pink-700 dark:text-pacific-blue-500 shadow-inner text-nowrap"
            for ul in main.find_all("ul"):
                ul["class"] = (
                    "prose prose-stone dark:prose-invert !w-full max-w-[40em] lg:max-w-[35em] list-disc pl-8 lg:prose-lg"
                )
                for code in ul.find_all("code"):
                    code["class"] = "p-1 text-pink-700 dark:text-pacific-blue-500 shadow-inner text-nowrap"
            for ol in main.find_all("ol"):
                ol["class"] = (
                    "prose prose-stone dark:prose-invert !w-full max-w-[40em] lg:max-w-[35em] list-decimal pl-8 lg:prose-lg"
                )
                for code in ol.find_all("code"):
                    code["class"] = "p-1 text-pink-700 dark:text-pacific-blue-500 shadow-inner text-nowrap"
            for table in main.find_all(
                "table", recursive=False
            ):  # Ne trouve que les table directement dans <main>
                table.parent["class"] = "prose-sm lg:prose-base prose-stone dark:prose-invert"
                for code in table.find_all("code"):
                    code["class"] = "p-1 text-pink-700 shadow-inner dark:text-pacific-blue-500 "
        sections = soup.find_all("section")
        if sections:
            for section in sections:
                for p in section.find_all(
                    "p", recursive=False
                ):  # Ne trouve que les <p> directement dans une section
                    p["class"] = "prose lg:prose-lg !w-full prose-stone  dark:prose-invert max-w-[40rem] mb-4"
        # 15. Subtitle
        for p in soup.find_all(
            "p", string=lambda text: text and text.startswith("|") and text.endswith("|")
        ):
            p["class"] = (
                "prose lg:prose-lg text-lg !mb-16 !w-full max-w-[40rem] text-gray-900 dark:text-gray-200 text-center".split(
                    " "
                )
            )
            p["role"] = "doc-subtitle"
            p.string = "“" + p.text.strip("|").strip() + "”"

            or_tag = soup.new_tag("p")
            or_tag["class"] = (
                "prose lg:prose-lg text-xl !w-full max-w-[40rem] !mb-6 !mt-2 text-gray-900 dark:text-gray-200 text-center".split(
                    " "
                )
            )
            or_tag.string = "— OR —"
            title_header.append(or_tag)
            title_header.append(p)

            meta = soup.new_tag("meta", attrs={
                "name": "description",
                "content": f"Today a blog post about '{p.text}'"
            })
            head.append(meta)
            break  # Only the first subtitle matter

        # Sauvegarder le fichier modifié
        out_file_path = file_path.parent / output_name if output_name else file_path
        with open(out_file_path, "w", encoding="utf-8"
        ) as file:
            file.write(str(soup))
        processed.append(file)
    print('\033[0m')
    if len(processed) == 0:
        print("\033[0;31mNo file found\033[0m")
    return processed


if __name__ == "__main__":
    help_line = "Usage: python modify_html.py <file_path> [<file_name> [<output_name>]]"
    if len(sys.argv) < 2:
        print(help_line)
        sys.exit(1)

    if sys.argv[1] == "--help":
        print(help_line)
    file_path = Path(sys.argv[1])
    html_file = None
    output_name = None
    if len(sys.argv) > 2:
        html_file = sys.argv[2]
        if len(sys.argv) == 4:
            output_name = sys.argv[3]
    processed = modify_html(file_path, html_file, output_name)
    for file in processed:
        print(f"Modifications apportées à {str(file.name)}")
