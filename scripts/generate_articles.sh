if [ $# -eq 1 ]; then
    echo $1
    if [ "$1" = "--regenerate" ]; then
        echo "\033[0;30mRegenerating...\033[0m"
        quarto render articles_jupyter/*.ipynb --to html
    fi
fi

if [ $? -eq 0 ]; then
    cp articles_jupyter/*.html public/articles && cp articles_jupyter/typoTest_files/libs/quarto-html/quarto-syntax-highlighting.css public/articles/quarto_files/libs/quarto-html/quarto-syntax-highlighting.css
    if [ $? -eq 0 ]; then
        cp articles_jupyter/typoTest_files/libs/quarto-html/quarto-syntax-highlighting-dark.css public/articles/quarto_files/libs/quarto-html/quarto-syntax-highlighting-dark.css
        if [ $? -ne 0 ]; then
            echo "\033[0;33mNo dark syntax highlighting found\033[0m"
        fi
        python3 ./scripts/quarto-translator.py public/articles
    else
        echo "\033[0;31mCopy failed\033[0m"
    fi
else
    echo "\033[0;31mGeneration failed\033[0m"
fi