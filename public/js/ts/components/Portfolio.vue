<template>
    <div class="w-full h-full select-none">
        <div class="max-w-6xl mx-auto">
            <ul ref="gallery" id="gallery" class="flex gap-6 flex-wrap mb-4 mt-8">
                <li v-for="(project, index) in projectGallery" :key="index"
                    class="h-56 w-56 flex-shrink-0 border-4 border-gray-900">
                    <div class="group relative h-full w-full p-2" @click="projectGalleryOpen(index, 0)">
                        <div class="h-full w-full overflow-hidden">
                            <img :src="project[0].image" :alt="project[0].alt"
                                class="cover min-w-full min-h-full mix-blend-multiply" />
                        </div>
                        <span class="tech-project">{{ project[0].title }}</span>
                    </div>
                </li>
            </ul>
        </div>

        <!-- Fullscreen Image Modal -->
        <div v-if="projectGalleryOpened" @click="projectGalleryClose"
            class="h-[100vh] w-[100vw] inset-0 fixed z-[99] bg-gray-900/85 cursor-zoom-out">
            <div class="relative flex items-center justify-center w-full h-full px-[1%] sm:px-[8%]">
                <!-- Previous Button -->
                <div v-if="projectGallery[curProjIdx].length > 1" @click.stop="projectGalleryPrev"
                    class="absolute left-4 select-none flex items-center justify-center text-gray-200 rounded-full cursor-pointer bg-gray-200/10 w-14 h-14 hover:bg-gray-200/20 -translate-y-[200%] xl:translate-y-0">
                    <svg class="w-6 h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                        stroke-width="3" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                    </svg>
                </div>

                <!-- Image Display -->
                <div class="flex flex-col xl:flex-row w-full h-screen max-h-screen justify-items-center gap-0">
                    <div class="w-full select-none h-2/3 max-h-2/3 xl:h-full ">
                        <img :src="projectGalleryActiveUrl"
                            class="mx-auto h-full object-contain block select-none cursor-zoom-out shadow-lg"
                            :alt='projectGallery[curProjIdx][curImageIdx].alt' />
                    </div>
                    <div @click.stop=""
                        class="h-full select-text xl:h-full w-full my-2 xl:my-0 text-gray-100 bg-gray-900/80 p-4 overflow-y-auto flex items-start xl:items-center">
                        <div>
                            <h1 class="text-pacific-blue-300 font-bold text-lg">{{
                                projectGallery[curProjIdx][curImageIdx].title }} :</h1>
                            <div class="" v-html="projectGallery[curProjIdx][curImageIdx].description.trim()"> </div>
                        </div>
                    </div>
                </div>

                <!-- Next Button -->
                <div v-if="projectGallery[curProjIdx].length > 1" @click.stop="projectGalleryNext"
                    class="absolute select-none right-4 flex items-center justify-center text-gray-200 rounded-full cursor-pointer bg-gray-200/10 w-14 h-14 hover:bg-gray-200/20 -translate-y-[200%] xl:translate-y-0">
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
import { defineComponent, defineProps, ref } from 'vue';

// Source : https://devdojo.com/pines/docs/image-gallery
export default defineComponent({
    name: 'ProjectGallery',
    props: {
        project_list: {
            type: Array as () => Array<{ image: string; alt: string; title: string; description: string }>[],
            required: true,
        },
    },
    setup(props) {
        const projectGalleryOpened = ref(false);
        const projectGalleryActiveUrl = ref<string | null>(null);
        const curImageIdx = ref<number | null>(null);
        const curProjIdx = ref<number>(0);

        const projectGallery = ref(props.project_list);
        const projectGalleryOpen = (projIndex: number, imgIndex: number) => {
            curProjIdx.value = projIndex;
            curImageIdx.value = imgIndex;
            projectGalleryActiveUrl.value = projectGallery.value[projIndex][imgIndex].image;
            projectGalleryOpened.value = true;
        };

        const projectGalleryClose = () => {
            projectGalleryOpened.value = false;
            setTimeout(() => (projectGalleryActiveUrl.value = null), 300);
        };

        const projectGalleryNext = () => {
            curImageIdx.value = (curImageIdx.value + 1) % projectGallery.value[curProjIdx.value].length;
            projectGalleryActiveUrl.value = projectGallery.value[curProjIdx.value][curImageIdx.value].image;
        };

        const projectGalleryPrev = () => {
            curImageIdx.value =
                (curImageIdx.value - 1 + projectGallery.value[curProjIdx.value].length) % projectGallery.value[curProjIdx.value].length;
            projectGalleryActiveUrl.value = projectGallery.value[curProjIdx.value][curImageIdx.value].image;
        };

        return {
            projectGalleryOpened,
            projectGalleryActiveUrl,
            curImageIdx,
            curProjIdx,
            projectGallery,
            projectGalleryOpen,
            projectGalleryClose,
            projectGalleryNext,
            projectGalleryPrev,
        };
    },
});
</script>
