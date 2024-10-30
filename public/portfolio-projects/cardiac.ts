const cardiac_projects = [
	{
		image: new URL(
			'../img/portfolio/cardiac/cto-coeur-details.png?width=800&as=webp&quality=90',
			import.meta.url,
		),
		alt: 'Diagram of cardiac anatomy',
		title: 'Mesuring Cardiac Strain',
		description: `
In 2021 I did my final Master's internship at the CREATIS lab.
I focused on studying cardiac function, specifically of the right ventricle.
The heart, a complex four-chamber organ, plays a vital role in pumping blood between the lungs and the body.
However, assessing the right ventricle is challenging due to its intricate shape. Long overlooked in clinical research,
the study of the right ventricle has proven essential for certain pathologies.
<br/><br/>
Right ventricular dysfunction — caused by high pressure, excess volume, or heart disease — remains difficult to evaluate with traditional imaging methods
like echocardiography and MRI, which provide only measurements for large surfaces and lack local precision.
Here, myocardial strain analysis offers a solution by quantifying local deformation and pinpointing problematic areas more accurately.
My work involved comparing different strain calculation techniques to better adapt these measurements to the unique characteristics of the right ventricle.
<br/><br/>
This research aims to refine diagnostic tools and provide physicians with more precise,
localized metrics, ultimately helping to improve patient care for those with cardiac conditions.
`,
	},
	{
		image: new URL(
			'../img/portfolio/cardiac/directions.png?width=800&as=webp&quality=90',
			import.meta.url,
		),
		alt: 'Results of vectors calculated using differents methods on the heart',
		title: 'Local Anatomical Direction Calculation of the Right Ventricle',
		description: `
In the right ventricle, the heart’s muscular fibers, or myocardial fibers, are arranged in specific patterns:
those near the inner wall (endocardium) run lengthwise, while those closer to the outer wall (epicardium) run around the heart.
These fiber orientations help the heart contract effectively. <br/>
To measure a contraction, we must know in which direction to measure it. Our goal is to mathematically identify directions that best match this natural fiber orientation to understand and measure heart function more accurately.
This will helps us model the natural directions of muscle contraction.
<br/><br/>
We focused on three main methods to compute these directions at each point:
<ul>
<li><b>Vector Operation (Long Axis Approach)</b>: Here, we use a vector from a midpoint between the valves to the apex (opposite to the valve) as a guide.
By calculating perpendicular vectors through cross-products, we approximate the fiber direction based on the heart’s overall shape.
This method is simple but less precise, as it relies on a single fixed axis.</li>
<li><b>Heat Diffusion</b>: Inspired by physical heat diffusion, this approach defines a "hot" point at the apex and “cold” points at the valves.
Solving the heat equation gives us the direction that increase the most, which mostly aligns with the heart's fibers.</li>
<li><b>Geodesic Distance</b>: Using the shortest path from each point to the valves, this method calculates the direction based on geodesic distances.
This approach adapts well to the heart's curved structure and provides directions that closely follow the muscle fiber layout.</li>
<br/><br/>
These methods together help us establish consistent 3D directional fields aligned with the heart's fiber orientation,
enhancing our ability to measure and interpret the mechanics of contraction.`,
	},
	{
		image: new URL(
			'../img/portfolio/cardiac/diffstrain.png?width=800&as=webp&quality=90',
			import.meta.url,
		),
		alt: 'Mean difference of the two strains on each point of the ventricle for two population (Healthy and Fallot)',
		title: 'Understanding Strain and Measuring It in Cardiac Deformation',
		description: `
<b>What is Strain?</b> Strain is a measure of how much something stretches or deforms.
For the heart, strain helps us measure how its shape changes as it contracts and relaxes.
Imagine measuring the length of a piece of muscle before and after it stretches; strain tells us
how much it’s changed compared to its original size.
<br/><br/>
We used two types of strain :
<ul>
    <li><b>Infinitesimal Strain</b>: As the name suggest, this approach works well for small deformations,
	giving us a good idea of changes in muscle shape. However, it’s less reliable with larger,
	more complex movements because it captures rotation, which can distort the strain value.</li>

    <li><b>Lagrangian Strain</b>: This type is better for measuring larger deformations and ignores rotation, focusing only on the actual stretching of the muscle.</li>
</ul>
<br/>
To confirm our ideas about the better strain we have to understand strain differences across healthy and affected heart populations.
We used methods that condense complex data into simpler patterns:
<ul>
    <li><b>Principal Component Analysis (PCA)</b> try to get the main ways of the strain change across the heart structure, highlighting how strain varies in key areas.</li>
    <li><b>Partial Least Squares (PLS)</b> focuses on trying to find the best way to split our data (healthy or not) using the strain. This allowed us to see that both strains are a good way to differentiate between the two populations.</li>
</ul>
This analysis confirmed that Lagrangian strain is more reliable because it ignores rotations, focusing purely on the muscle’s stretch, making it especially useful for detecting heart conditions.
`,
	},
	{
		image: new URL(
			'../img/portfolio/cardiac/interest.png?width=800&as=webp&quality=90',
			import.meta.url,
		),
		alt: 'Histogram of the interest of the query "myocardial strain" on pubmed from 1951 to 2021. We can see a huge increase of interest those last few year.',
		title: 'Wrapping it Up: ',
		description: `
So, after all that, what did we learn from our journey through right ventricle analysis?
First, we explored different ways to map out anatomical directions. By testing a few options, we decided that using the heat equation
followed the anatomical reality better than anything else, and - as a bonus - it’s straightforward to calculate.
<br/><br/>
Then we dove into strain, a measure of stretchiness.
We tested our strain methods individually and at a population level, finding that tricuspid valve rotation could throw off the infinitesimal strain,
which led us to vote in favor of Lagrangian strain. We also confirmed strain is a good indicator of unhealthy heart movement patterns.
<br/><br/>
In the end, strain gives us a detailed look into what we want from the ventricle: its pumping power.
Ejection fraction (EF) is a helpful, widely used number, but it's a big-picture view—like reading a headline instead of the whole story.
EF tells us if there's a problem, but strain digs deeper, pointing out exactly where things might be going bad.
Strain gives us insight that lets us track each heart muscle fiber's specific movements, and these informations can make a big difference in understanding heart function.
<br/><br/>
So, here’s our takeaway: choosing directions based on anatomy and a reliable local strain measure gives us a clear, practical view of cardiac function.
This journey’s far from over, researchers and the industry are working to unite all these strain approaches.
Our work is just one step forward in this quest for a truly comprehensive view of the heart.
I was lucky enough to contribute - through this work - to 2 research papers focusing on this goal :
<ul>
<li>"<b>Which anatomical directions to quantify local right ventricular strain in 3D echocardiography?</b>" by M Di Folco, T Dargent, G Bernardino, P Clarysse, N Duchateau</li>
<li>"<b>Strainger things: discrete differential geometry for transporting right ventricular deformation across meshes</b>" by G Bernardino, T Dargent, O Camara, N Duchateau</li>
</ul>
This experience allowed me to better undestand discrete geometry, population analysis and also, unsurprisingly, cardiology. I surprised myself by talking with my med student roommate about cardiac pathologies, and understanding the terms he threw at me.
One of my best work experience, with the nicest team on earth.
`,
	},
];

export default cardiac_projects;
