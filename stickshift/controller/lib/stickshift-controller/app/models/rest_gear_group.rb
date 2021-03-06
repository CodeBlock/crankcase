class RestGearGroup < StickShift::Model
  attr_accessor :name, :gear_profile, :cartridges, :gears

  def initialize(group_instance, gear_states = {})
    app               = group_instance.app
    self.name         = group_instance.name
    self.gear_profile = group_instance.node_profile
    self.gears        = group_instance.gears.map{ |gear| {:id => gear.uuid, :state => gear_states[gear.uuid] || 'unknown'} }
    self.cartridges   = group_instance.component_instances.map { |comp_inst| app.comp_instance_map[comp_inst].cart_properties.merge({:name => app.comp_instance_map[comp_inst].parent_cart_name}) }
    self.cartridges.delete_if{ |comp| comp[:name] == app.name }
  end

  def to_xml(options={})
    options[:tag_name] = "gear_group"
    super(options)
  end
end
