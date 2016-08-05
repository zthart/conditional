import SimpleMasonry from "simple-masonry";
import FreqencyMap from "../models/frequencyMap";
import Exception from "../exceptions/exception";
import MasonryException from "../exceptions/masonryException";

export default class Masonry {
  constructor(grid) {
    this.grid = grid;

    this.masonry = new SimpleMasonry({
      masonryBox: this.grid,
      masonryColumn: this._findSharedSelector(this.grid)
    });

    this.render();
  }

  render() {
    this.masonry.init();
  }

  _findSharedSelector(parent) {
    let selectors = new FreqencyMap();
    let sharedSelector = null;

    try {
      parent.childNodes.forEach(child => {
        if (typeof child.tagName !== "undefined" &&
            child.tagName !== null &&
            child.tagName !== "") {
          selectors.increment(child.tagName);
        }

        if (typeof child.id !== "undefined" &&
            child.id !== null &&
            child.id !== "") {
          selectors.increment("#" + child.id);
        }

        if (typeof child.className !== "undefined" &&
            child.className !== null &&
            child.className !== "") {
          child.className.split(/\s+/).forEach(className => {
            selectors.increment("." + className);
          });
        }
      });

      sharedSelector = selectors.getHighest();
    } catch (e) {
      throw new Exception(
        MasonryException.CANT_FIND_SHARED_SELECTOR,
        e.message
      );
    }

    if (sharedSelector === null) {
      throw new Exception(MasonryException.CANT_FIND_SHARED_SELECTOR);
    } else {
      return sharedSelector;
    }
  }
}
