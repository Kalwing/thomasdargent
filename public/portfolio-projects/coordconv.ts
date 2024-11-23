const cardiac_projects = [
	{
		image: new URL(
			'../img/portfolio/coordconv/coordconv_block.webp?width=800&as=webp&quality=90',
			import.meta.url,
		),
		thumbnail: new URL(
			'../img/portfolio/coordconv/coordconv_block.webp?width=250&as=webp&quality=75',
			import.meta.url,
		),
		alt: 'Diagram of how a CoordConv block works (adding coordinates layer to the image before the convolution)',
		title: 'CoordConv : A Map for Learning',
		description: `
As we know, adding regularization smooths out the learning space, allowing us to train with fewer data points.
This is essential for medical images, which often have very small datasets, and needs every trick in the book to learn better.
<b>CoordConv</b> isn't a regularization factor per se, but has a similar effect by adding informations to the input. It adds coordinates, kinda like a built in map, to a
convolutional neural network (CNN) alongside the image.
Hopefully giving a better notion of spatial structure to the network.<br/>
We know the body follow a very geometrically structured pattern : The heart is on the left, the lungs in the center, etc..
As such it seems relevant to focus on the objects location for learning.
<br/><br/>
We focused on two dataset: Segthor, for thoracic organs, and ACDC, specifically for the heart.
The loss function was regularized with a size constraint, as defined by <b>Hoel Kervadec</b> (with whom I had the chance to work at LIVIA in Canada)
<br/><br/>
In the end it didn't create a massive leap on the overall results, but it did lead to a <b>marginally better convergence</b> which is very important.
This suggests it might be a <b>cheap and useful addition</b> to any convolutionnal neural network focused on medical images.
<br/><br/>
That's where I left it. <b>Rosana El Jurdi</b>, my co-author, pushed the idea further by using other losses (like skeleton loss).
They did experiments on other datasets and noticed a huge improvement on segmentation scores too. A nice and cheap addition indeed!
`,
	},
];

export default cardiac_projects;
