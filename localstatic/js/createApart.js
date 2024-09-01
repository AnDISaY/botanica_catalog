function createEl(resp) {
    apart = document.createElement("div");
    apart.classList.add("project-apartments__apart");
    tags = document.createElement("div");
    tags.classList.add("project-apartments__apart__tags");
    tag = document.createElement("div");
    tag.classList.add("project-apartments__apart__tag");
    tag.innerHtml = resp.
    tag2 = document.createElement("div");
    tag2.classList.add("project-apartments__apart__tag");
    tags.appendChild(tag);
    tags.appendChild(tag2);
    apart.appendChild(tags);
    console.log(apart)
    document.getElementsByTagName('body').appendChild(apart)
    resp.querySelectorAll('.project-apartments__apart')
    console.log(resp)
}