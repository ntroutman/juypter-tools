import IPython.display


def image_table(labels_with_images, width=120, height=80):
    """Creates a 2-column image table with labels on left and images on the right. Images can
    be any image type compatible with by IPython.display.Image.

        labels_with_images - iterable of (label, image) tuples
        width - image width
        height - image height

    Example:

    >>> image_path = "data/blur-detection/scifi-1-no-blur.jpg"
    >>> cv2_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    >>> display(image_table([
        ("from file", image_path),
        ("cv2", cv2_image)
    ]))
    """
    output = "<table>"
    for label, images in labels_with_images:
        if not isinstance(images, (list, tuple)):
            images = [images]
        image_html = ""
        for image in images:
            image = IPython.display.Image(image, height=height, width=width)
            mime_info, _ = image._repr_mimebundle_()
            mimetype, b64_data = next(iter(mime_type.items()))
            image_html += f'<img style="float:left" src="data:{mimetype};base64,{b64_data}" width="{width}" height="{height}">'
        output += f"<tr><td>{label}</td><td>{image_html}</td></tr>"
    output += "</table>"
    return IPython.display.HTML(output)
