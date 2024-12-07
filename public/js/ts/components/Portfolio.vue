<template>
    <div class="w-full h-full select-none">
        <div class="max-w-6xl mx-auto">
            <ul ref="gallery" id="gallery" class="flex gap-6 flex-wrap mb-4 mt-8">
                <li v-for="(project, index) in project_list" :key="index"
                    class="h-56 w-56 flex-shrink-0 border-4 border-gray-900 dark:border-pink-600">
                    <div class="group relative h-full w-full p-2" tabindex="0" @click="projectGalleryOpen(index, 0)"
                        @keyup.enter="projectGalleryOpen(index, 0)">
                        <div class="h-full w-full overflow-hidden relative">
                            <img :src="project[0].thumbnail.toString()" :alt="project[0].alt"
                                class="cover min-w-full min-h-full mix-blend-multiply dark:mix-blend-luminosity dark:bg-pink-400" />
                            <div
                                class="hidden dark:block absolute top-0 left-0 h-full w-full dark:bg-pink-800 mix-blend-color opacity-50">
                            </div>
                        </div>
                        <span
                            class="tech-project dark:bg-gray-1000 dark:rounded-full dark:border-2 dark:border-pink-600 dark:text-gray-200 dark:px-5 dark:py-1">{{
                                project[0].title }}</span>
                    </div>
                </li>
            </ul>
        </div>

        <!-- Fullscreen Image Modal -->
        <div id="portfolio" v-if="projectGalleryOpened" @click="projectGalleryClose" @keyup.esc="projectGalleryClose"
            @keyup.left="projectGalleryPrev" @keyup.right="projectGalleryNext" tabindex="-1" autofocus
            class="h-[100vh] w-[100vw] inset-0 fixed z-[99] bg-gray-900/85 dark:bg-gray-1000/90 backdrop-blur-sm cursor-zoom-out outline-none">
            <div class="relative flex items-center justify-center w-full h-full px-[1%] sm:px-[8%]">
                <!-- Previous Button -->
                <div v-if="project_list[curProjIdx].length > 1" tabindex="0" @click.stop="projectGalleryPrev"
                    @keyup.enter="projectGalleryPrev"
                    class="absolute left-4 select-none flex items-center justify-center text-pacific-blue-500 rounded-full cursor-pointer bg-gray-900/20 w-10 h-10 hover:bg-gray-900/30 dark:border dark:border-pink-600 dark:text-pink-400 -translate-y-[275%] xl:translate-y-0">
                    <svg class="w-6 h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                        stroke-width="3" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                    </svg>
                </div>

                <!-- Image Display -->
                <div class="flex flex-col xl:flex-row w-full h-screen max-h-screen justify-items-center gap-0">
                    <div class="w-full select-none h-2/3 max-h-2/3 xl:h-full flex content-center">
                        <img :src="projectGalleryActiveUrl"
                            class="mx-auto max-h-full object-contain block select-none cursor-zoom-out"
                            :alt='project_list[curProjIdx][curImageIdx].alt' />
                    </div>
                    <div @click.stop="" id="portfolio-text"
                        class="h-full select-text xl:h-full w-full my-2 xl:my-0 text-gray-100 bg-gray-900/80 dark:bg-gray-1000 dark:text-gray-200 p-4 overflow-y-auto flex items-start xl:items-center cursor-default">
                        <div>
                            <h1 class="text-pacific-blue-300 font-bold text-lg">{{
                                project_list[curProjIdx][curImageIdx].title }} :</h1>
                            <div class="[&_ul]:list-disc [&_ul]:pl-5 [&_b]:text-pacific-blue-100 [&_b]:font-bold [&_h2]:text-pacific-blue-500 pb-8"
                                v-html="project_list[curProjIdx][curImageIdx].description.trim()"> </div>
                        </div>
                    </div>
                </div>

                <!-- Next Button -->
                <div v-if="project_list[curProjIdx].length > 1" tabindex="0" @click.stop="projectGalleryNext"
                    @keyup.enter="projectGalleryPrev"
                    class="absolute select-none right-4 flex items-center justify-center text-pacific-blue-500 rounded-full cursor-pointer bg-gray-900/20 w-10 h-10 hover:bg-gray-900/30 dark:border dark:border-pink-600 dark:text-pink-400 -translate-y-[275%] xl:translate-y-0">
                    <svg class="w-6 h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                        stroke-width="3" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                    </svg>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    name: 'Portfolio'
};
</script>
<script setup lang="ts">
import { ref, nextTick } from 'vue';

interface ProjectImage {
    image: URL;
    thumbnail: URL;
    alt: string;
    title: string;
    description: string;
}

interface Props {
    project_list: ProjectImage[][]
}

const props = defineProps<Props>();

const projectGalleryOpened = ref(false);
const projectGalleryActiveUrl = ref<string>("");
const curImageIdx = ref(0);
const curProjIdx = ref(0);


const projectGalleryOpen = (projIndex: number, imgIndex: number) => {
    curProjIdx.value = projIndex;
    curImageIdx.value = imgIndex;
    projectGalleryActiveUrl.value = props.project_list[projIndex][imgIndex].image.toString();
    projectGalleryOpened.value = true;
    nextTick(() => {
        const portfolio = document.getElementById('portfolio');

        if (portfolio) {
            // Force element to be focusable
            portfolio.focus({ preventScroll: true });
            console.log('Focus:', document.activeElement === portfolio);
        }
    });
};

const projectGalleryClose = () => {
    projectGalleryOpened.value = false;
    setTimeout(() => (projectGalleryActiveUrl.value = ""), 300);
};

const projectGalleryNext = () => {
    curImageIdx.value = (curImageIdx.value + 1) % props.project_list[curProjIdx.value].length;
    projectGalleryActiveUrl.value = props.project_list[curProjIdx.value][curImageIdx.value].image.toString();
    const portfolioText = document.getElementById('portfolio-text');
    if (portfolioText) portfolioText.scrollTop = 0;
};

const projectGalleryPrev = () => {
    curImageIdx.value =
        (curImageIdx.value - 1 + props.project_list[curProjIdx.value].length) % props.project_list[curProjIdx.value].length;
    projectGalleryActiveUrl.value = props.project_list[curProjIdx.value][curImageIdx.value].image.toString();
    const portfolioText = document.getElementById('portfolio-text');
    if (portfolioText) portfolioText.scrollTop = 0;
};


addEventListener("keyup", (key) => {
    console.log("Touch")
    if (projectGalleryOpened) {
        if (key.code == "Escape") {
            projectGalleryClose()
        }
        else if (key.code == "ArrowRight") {
            projectGalleryNext()
        }
        else if (key.code == "ArrowLeft") {
            projectGalleryPrev()
        }
    }
});

</script>
